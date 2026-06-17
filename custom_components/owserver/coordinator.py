from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from xml.etree import ElementTree

import aiohttp

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, DETAILS_XML_PATH

_LOGGER = logging.getLogger(__name__)


class OWServerCoordinator(DataUpdateCoordinator):
    def __init__(
        self,
        hass: HomeAssistant,
        host: str,
        port: int,
        username: str | None,
        password: str | None,
        poll_interval: int,
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=poll_interval),
        )
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self._base_url = f"http://{host}:{port}"
        self._auth = None
        if username and password:
            self._auth = aiohttp.BasicAuth(username, password)

    async def _async_update_data(self) -> dict:
        url = f"{self._base_url}{DETAILS_XML_PATH}"
        try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with aiohttp.ClientSession(auth=self._auth, timeout=timeout) as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    text = await response.text()
                    if text.strip().startswith("<"):
                        return self._parse_xml(text)
                    return self._parse_csv(text)
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with OW-SERVER: {err}") from err
        except (TimeoutError, asyncio.TimeoutError) as err:
            raise UpdateFailed(f"Timeout communicating with OW-SERVER: {err}") from err

    def _parse_xml(self, xml_text: str) -> dict:
        import re
        xml_text = re.sub(r'\s+xmlns(:\w+)?="[^"]*"', "", xml_text, count=1)
        root = ElementTree.fromstring(xml_text)
        devices = {}

        for child in root:
            tag = child.tag
            if not tag.startswith("owd_"):
                continue
            device_type = tag[4:]
            rom_id = None
            dev_info = {
                "type": device_type,
                "description": child.get("Description", ""),
                "sensors": {},
            }

            for elem in child:
                if elem.tag == "ROMId":
                    rom_id = elem.text
                    dev_info["rom_id"] = rom_id
                elif elem.tag == "Name":
                    dev_info["name"] = elem.text
                elif elem.tag == "Family":
                    dev_info["family"] = elem.text
                elif elem.tag == "Channel":
                    dev_info["channel"] = elem.text
                elif elem.tag == "Health":
                    dev_info["health"] = elem.text
                elif elem.tag in ("Temperature", "Humidity", "Pressure", "Light",
                                  "DewPoint", "HeatIndex", "LightLevel"):
                    val = self._parse_value(elem.text, elem.get("Units"))
                    if val is not None:
                        dev_info["sensors"][elem.tag] = val

            if not dev_info["sensors"]:
                for elem in child:
                    if elem.tag == "PrimaryValue":
                        val = self._parse_value(elem.text, elem.get("Units"))
                        if val is not None:
                            dev_info["sensors"]["Temperature"] = val
                        break

            if rom_id:
                devices[rom_id] = dev_info

        return devices

    def _parse_csv(self, text: str) -> dict:
        tokens = text.split()
        devices = {}

        idx = 0
        while idx < len(tokens):
            t = tokens[idx]
            if t in ("DS18B20", "DS18S20", "DS1822", "DS1820", "DS2438", "DS2406",
                     "DS2408", "DS2423", "DS2450", "DS2405", "DS2413", "DS28EA00",
                     "DS1921", "DS1920") or t.startswith("EDS"):
                if idx + 13 < len(tokens) and len(tokens[idx + 2]) >= 14:
                    break
            idx += 1

        while idx + 13 < len(tokens):
            device_type = tokens[idx]
            family = tokens[idx + 1]
            rom_id = tokens[idx + 2]
            health = tokens[idx + 3]
            channel = tokens[idx + 4]
            raw_data = tokens[idx + 5]
            primary_val_num = tokens[idx + 6]
            primary_val_unit1 = tokens[idx + 7]
            primary_val_unit2 = tokens[idx + 8]
            temperature = tokens[idx + 9]
            user_byte1 = tokens[idx + 10]
            user_byte2 = tokens[idx + 11]
            resolution = tokens[idx + 12]
            power_source = tokens[idx + 13]

            primary_unit = f"{primary_val_unit1} {primary_val_unit2}"
            sensors = {}

            try:
                sensors["Temperature"] = {
                    "value": float(temperature),
                    "unit": primary_unit,
                }
            except ValueError:
                pass

            try:
                sensors["PrimaryValue"] = {
                    "value": float(primary_val_num),
                    "unit": primary_unit,
                }
            except ValueError:
                pass

            dev_info = {
                "type": device_type,
                "family": family,
                "rom_id": rom_id,
                "health": health,
                "channel": channel,
                "name": f"{device_type} ({rom_id[-4:]})",
                "sensors": sensors,
            }

            devices[rom_id] = dev_info
            idx += 14

        return devices

    def _parse_value(self, text: str | None, unit: str | None) -> dict | None:
        if text is None:
            return None
        text = text.strip()
        if not text:
            return None
        try:
            return {"value": float(text), "unit": unit}
        except ValueError:
            parts = text.split(" ", 1)
            try:
                return {"value": float(parts[0]), "unit": parts[1] if len(parts) > 1 else unit}
            except (ValueError, IndexError):
                return None
