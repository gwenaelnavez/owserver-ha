from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry

from .const import DOMAIN
from .coordinator import OWServerCoordinator


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    coordinator: OWServerCoordinator = hass.data[DOMAIN][entry.entry_id]
    return {
        "host": coordinator.host,
        "port": coordinator.port,
        "devices": coordinator.data,
    }


async def async_get_device_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry
) -> dict[str, Any]:
    coordinator: OWServerCoordinator = hass.data[DOMAIN][entry.entry_id]
    rom_id = list(device.identifiers)[0][1] if device.identifiers else None
    device_data = coordinator.data.get(rom_id, {}) if rom_id else {}
    return {
        "host": coordinator.host,
        "device_rom_id": rom_id,
        "device_info": device_data,
    }
