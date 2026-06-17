# OW-SERVER (EDS) for Home Assistant

Home Assistant integration for [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), a 1-Wire to Ethernet server.

## Features

- Discovers all connected 1-Wire sensors automatically
- Supports DS18B20, DS18S20, DS1822, DS2438, and EDS sensors (EDS0064, EDS0065, EDS0066, EDS0067, EDS0068, etc.)
- Creates individual sensor entities for each measurement (Temperature, Humidity, Pressure, Light)
- Groups sensors by physical device in the device registry
- Configurable polling interval (default: 30s)
- Supports authenticated connections
- Handles both XML and CSV response formats

## Installation

### HACS (recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots in the top right and select "Custom repositories"
4. Add `https://github.com/gwenaelnavez/owserver-ha` as a custom repository (category: Integration)
5. Click "Install"
6. Restart Home Assistant

### Manual

1. Copy the `custom_components/owserver/` directory to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant

## Configuration

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for **OW-SERVER (EDS)**
4. Enter your OW-SERVER details:
   - **Host**: IP address or hostname
   - **Port**: 80 (default)
   - **Username**: admin (default)
   - **Password**: eds (default)

## Supported Sensors

| Family | Type | Measurements |
|--------|------|-------------|
| DS18B20 | Temperature Sensor | Temperature |
| DS18S20 | Temperature Sensor | Temperature |
| DS1822 | Temperature Sensor | Temperature |
| EDS0064 | Temperature Sensor | Temperature |
| EDS0065 | Temperature + Humidity | Temperature, Humidity |
| EDS0066 | Temperature + Pressure | Temperature, Pressure |
| EDS0067 | Temperature + Light | Temperature, Light |
| EDS0068 | Temp + Humidity + Pressure + Light | Temperature, Humidity, Pressure, Light |
| EDS0071/0072 | RTD Temperature | Temperature |

## License

MIT
