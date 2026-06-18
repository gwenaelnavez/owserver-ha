from __future__ import annotations

import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import OWServerCoordinator

_LOGGER = logging.getLogger(__name__)

UNIT_MAP = {
    "Centigrade": "°C",
    "PercentRelativeHumidity": PERCENTAGE,
    "Millibar": "mbar",
    "Lux": "lx",
    "Deg C": "°C",
    "Celsius": "°C",
    "Deg F": "°F",
    "Fahrenheit": "°F",
}

DEVICE_CLASS_MAP = {
    "Temperature": SensorDeviceClass.TEMPERATURE,
    "Humidity": SensorDeviceClass.HUMIDITY,
    "Pressure": SensorDeviceClass.PRESSURE,
    "Light": SensorDeviceClass.ILLUMINANCE,
    "LightLevel": SensorDeviceClass.ILLUMINANCE,
    "DewPoint": SensorDeviceClass.TEMPERATURE,
    "HeatIndex": SensorDeviceClass.TEMPERATURE,
}

STATE_CLASS_MAP = {
    SensorDeviceClass.TEMPERATURE: SensorStateClass.MEASUREMENT,
    SensorDeviceClass.HUMIDITY: SensorStateClass.MEASUREMENT,
    SensorDeviceClass.PRESSURE: SensorStateClass.MEASUREMENT,
    SensorDeviceClass.ILLUMINANCE: SensorStateClass.MEASUREMENT,
}

ICON_MAP = {
    "Temperature": "mdi:thermometer",
    "Humidity": "mdi:water-percent",
    "Pressure": "mdi:gauge",
    "Light": "mdi:brightness-5",
    "LightLevel": "mdi:brightness-5",
    "DewPoint": "mdi:thermometer-water",
    "HeatIndex": "mdi:thermometer",
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: OWServerCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []

    for rom_id, dev_info in coordinator.data.items():
        sensor_name = dev_info.get("name") or dev_info.get("type", "Unknown")
        for sensor_tag, sensor_val in dev_info["sensors"].items():
            entities.append(
                OWServerSensor(coordinator, rom_id, sensor_name, sensor_tag, sensor_val)
            )

    async_add_entities(entities)


class OWServerSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: OWServerCoordinator,
        rom_id: str,
        device_name: str,
        sensor_tag: str,
        sensor_val: dict,
    ) -> None:
        super().__init__(coordinator)
        self._rom_id = rom_id
        self._sensor_tag = sensor_tag
        self._attr_unique_id = f"{rom_id}_{sensor_tag}"
        self._attr_name = sensor_tag

        device_class = DEVICE_CLASS_MAP.get(sensor_tag)
        self._attr_device_class = device_class
        if device_class in STATE_CLASS_MAP:
            self._attr_state_class = STATE_CLASS_MAP[device_class]

        if sensor_tag in ICON_MAP:
            self._attr_icon = ICON_MAP[sensor_tag]

        unit = sensor_val.get("unit")
        if unit in UNIT_MAP:
            self._attr_native_unit_of_measurement = UNIT_MAP[unit]
        elif device_class == SensorDeviceClass.TEMPERATURE:
            self._attr_native_unit_of_measurement = "°C"

        dev = coordinator.data.get(rom_id, {})
        model = dev.get("type", "Unknown")
        channel = dev.get("channel")
        health = dev.get("health")

        self._attr_extra_state_attributes = {
            "rom_id": rom_id,
            "channel": channel,
            "health": health,
        }

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, rom_id)},
            name=f"{model} ({rom_id})",
            manufacturer="EDS",
            model=model,
            sw_version="1.0",
            via_device=(DOMAIN, coordinator.host),
        )

    @property
    def native_value(self):
        data = self.coordinator.data.get(self._rom_id)
        if data is None:
            return None
        sensor = data["sensors"].get(self._sensor_tag)
        if sensor is None:
            return None
        return sensor.get("value")


def dev_info_type(coordinator: OWServerCoordinator, rom_id: str) -> str:
    dev = coordinator.data.get(rom_id, {})
    return dev.get("type", "Unknown")
