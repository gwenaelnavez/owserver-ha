from __future__ import annotations

from pathlib import Path

from aiohttp import web

from homeassistant.components.http import HomeAssistantView
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
    DOMAIN,
    CONF_POLL_INTERVAL,
    CONF_ENABLE_PANEL,
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

    if entry.data.get(CONF_ENABLE_PANEL, True):
        _async_register_panel(hass)

    return True


def _async_register_panel(hass: HomeAssistant) -> None:
    from homeassistant.components.frontend import (
        async_register_built_in_panel,
    )

    panel_dir = Path(__file__).parent / "panel"

    class OWServerPanelView(HomeAssistantView):
        requires_auth = False
        url = "/api/owserver/panel"
        name = "api:owserver:panel"

        async def get(self, request):
            text = await hass.async_add_executor_job(
                lambda: (panel_dir / "panel.html").read_text(encoding="utf-8")
            )
            return web.Response(text=text, content_type="text/html")

    hass.http.register_view(OWServerPanelView)

    async_register_built_in_panel(
        hass=hass,
        component_name="iframe",
        sidebar_title="OW-SERVER",
        sidebar_icon="mdi:thermometer",
        frontend_url_path="owserver",
        config={
            "url": "/api/owserver/panel",
        },
        require_admin=False,
        update=True,
    )


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    from homeassistant.components.frontend import async_remove_panel

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        async_remove_panel(hass, "owserver")
    return unload_ok
