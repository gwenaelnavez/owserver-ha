[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md)

# 🌡️ OW-SERVER (EDS) for Home Assistant

Home Assistant integration for [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), a 1-Wire to Ethernet server. Automatically discovers and monitors all connected 1-Wire sensors.

---

## ✨ Features

- **🔍 Auto-discovery** – Detects all connected 1-Wire sensors automatically
- **🌡️ Multi-sensor support** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Per-measurement entities** – Temperature, Humidity, Pressure, Light as individual sensors
- **📦 Physical device grouping** – Sensors grouped by device in HA device registry
- **⏱️ Configurable polling** – Default 30s interval
- **🔐 Authenticated connections** – Supports username/password login
- **📄 Dual format** – Handles both XML and CSV response formats

---

## 📥 Installation

<details>
<summary><b>HACS (recommended)</b></summary>

1. Open HACS in Home Assistant
2. Go to **Integrations**
3. Click the three dots in the top right and select **Custom repositories**
4. Add `https://github.com/gwenaelnavez/owserver-ha` as a custom repository (category: **Integration**)
5. Click **Install**
6. Restart Home Assistant

</details>

<details>
<summary><b>Manual</b></summary>

1. Copy the `custom_components/owserver/` directory to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

</details>

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for **OW-SERVER (EDS)**
4. Enter your OW-SERVER details:

| Parameter | Default | Description |
|-----------|---------|-------------|
| **Host** | – | IP address or hostname |
| **Port** | `80` | HTTP port |
| **Username** | `admin` | Login username |
| **Password** | `eds` | Login password |

---

## 🔌 Supported Sensors

| Family | Type | Measurements |
|--------|------|-------------|
| DS18B20 | 🌡️ Temperature Sensor | Temperature |
| DS18S20 | 🌡️ Temperature Sensor | Temperature |
| DS1822 | 🌡️ Temperature Sensor | Temperature |
| EDS0064 | 🌡️ Temperature Sensor | Temperature |
| EDS0065 | 🌡️💧 Temp + Humidity | Temperature, Humidity |
| EDS0066 | 🌡️📊 Temp + Pressure | Temperature, Pressure |
| EDS0067 | 🌡️☀️ Temp + Light | Temperature, Light |
| EDS0068 | 🌡️💧📊☀️ Temp + Humidity + Pressure + Light | Temperature, Humidity, Pressure, Light |
| EDS0071/0072 | 🌡️ RTD Temperature | Temperature |

---

## 📁 Repository Structure

```
custom_components/owserver/
├── __init__.py       # Integration setup
├── config_flow.py    # Config flow UI
├── const.py          # Constants
├── coordinator.py    # Data update coordinator
├── diagnostics.py    # Diagnostics support
├── manifest.json     # Integration manifest
├── sensor.py         # Sensor platform
├── services.yaml     # Service definitions
└── strings.json      # Translation strings
```

---

## 📄 License

MIT
