from __future__ import annotations

import asyncio
import logging
import re
from xml.etree import ElementTree

import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
    DEFAULT_PORT,
    DEFAULT_USERNAME,
    DEFAULT_PASSWORD,
    DETAILS_XML_PATH,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Optional(CONF_USERNAME, default=DEFAULT_USERNAME): str,
        vol.Optional(CONF_PASSWORD, default=DEFAULT_PASSWORD): str,
    }
)

KNOWN_DEVICE_TYPES = frozenset({
    "DS18B20", "DS18S20", "DS1822", "DS1820", "DS2438",
    "DS2406", "DS2408", "DS2423", "DS2450",
})


async def validate_connection(hass: HomeAssistant, data: dict) -> list:
    host = data[CONF_HOST]
    port = data.get(CONF_PORT, DEFAULT_PORT)
    username = data.get(CONF_USERNAME)
    password = data.get(CONF_PASSWORD)

    base_url = f"http://{host}:{port}"
    url = f"{base_url}{DETAILS_XML_PATH}"

    auth = None
    if username and password:
        auth = aiohttp.BasicAuth(username, password)

    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(auth=auth, timeout=timeout) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()

            if text.strip().startswith("<"):
                text = re.sub(r'\s+xmlns(:\w+)?="[^"]*"', "", text, count=1)
                root = ElementTree.fromstring(text)
                devices = []
                for child in root:
                    if child.tag.startswith("owd_"):
                        rom_id = None
                        name = None
                        for elem in child:
                            if elem.tag == "ROMId":
                                rom_id = elem.text
                            elif elem.tag == "Name":
                                name = elem.text
                        if rom_id:
                            devices.append({
                                "rom_id": rom_id,
                                "name": name or child.tag[4:],
                            })
                return devices

            tokens = text.split()
            devices = []
            idx = 0
            while idx < len(tokens):
                t = tokens[idx]
                if t in KNOWN_DEVICE_TYPES or t.startswith("EDS"):
                    if idx + 13 < len(tokens) and len(tokens[idx + 2]) >= 14:
                        break
                idx += 1
            while idx + 13 < len(tokens):
                rom_id = tokens[idx + 2]
                device_type = tokens[idx]
                devices.append({
                    "rom_id": rom_id,
                    "name": f"{device_type} ({rom_id})",
                })
                idx += 14
            return devices


class OWServerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_HOST])
            self._abort_if_unique_id_configured()

            try:
                devices = await validate_connection(self.hass, user_input)
                if not devices:
                    errors["base"] = "no_devices"
                else:
                    return self.async_create_entry(
                        title=user_input[CONF_HOST],
                        data=user_input,
                    )
            except aiohttp.ClientError:
                errors["base"] = "cannot_connect"
            except ElementTree.ParseError:
                errors["base"] = "invalid_xml"
            except (TimeoutError, asyncio.TimeoutError):
                errors["base"] = "timeout"
            except Exception:
                _LOGGER.exception("Unexpected error during config flow")
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
