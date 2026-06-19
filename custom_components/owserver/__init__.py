from __future__ import annotations

from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
    DOMAIN,
    CONF_POLL_INTERVAL,
    DEFAULT_PORT,
    DEFAULT_POLL_INTERVAL,
)
from .coordinator import OWServerCoordinator

PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})

    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_PORT, DEFAULT_PORT)
    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)
    poll_interval = entry.data.get(CONF_POLL_INTERVAL, DEFAULT_POLL_INTERVAL)

    coordinator = OWServerCoordinator(
        hass, host, port, username, password, poll_interval
    )

    try:
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:
        raise ConfigEntryNotReady(f"Failed to connect to OW-SERVER: {err}") from err

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    await _async_register_panel(hass)

    return True


async def _async_register_panel(hass: HomeAssistant) -> None:
    from homeassistant.components.frontend import async_register_built_in_panel

    panel_path = str(Path(__file__).parent / "panel")

    hass.http.register_static_path(
        "/static/owserver",
        panel_path,
        cache_headers=False,
    )

    await async_register_built_in_panel(
        hass=hass,
        component_name="custom-panel",
        sidebar_title="OW-SERVER",
        sidebar_icon="mdi:thermometer",
        url_path="owserver",
        config={
            "_panel_custom": {
                "name": "owserver-panel",
                "module_url": "/static/owserver/panel.html",
                "embed_iframe": True,
            }
        },
        require_admin=False,
    )


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
