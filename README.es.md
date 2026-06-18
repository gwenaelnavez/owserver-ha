[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md) | [Italiano](README.it.md)

# 🌡️ OW-SERVER (EDS) para Home Assistant

Integración de Home Assistant para [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), un servidor 1-Wire a Ethernet. Descubre y monitorea automáticamente todos los sensores 1-Wire conectados.

---

## ✨ Características

- **🔍 Auto-descubrimiento** – Detecta automáticamente todos los sensores 1-Wire conectados
- **🌡️ Multi-sensor** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Entidades por medición** – Temperatura, Humedad, Presión, Luz como sensores individuales
- **📦 Agrupación física** – Sensores agrupados por dispositivo en el registro de dispositivos
- **⏱️ Polling configurable** – Intervalo predeterminado de 30s
- **🔐 Conexiones autenticadas** – Soporta inicio de sesión con usuario/contraseña
- **📄 Formato dual** – Procesa respuestas XML y CSV

---

## 📥 Instalación

<details>
<summary><b>HACS (recomendado)</b></summary>

1. Abra HACS en Home Assistant
2. Vaya a **Integraciones**
3. Haga clic en los tres puntos en la esquina superior derecha y seleccione **Repositorios personalizados**
4. Agregue `https://github.com/gwenaelnavez/owserver-ha` como repositorio personalizado (categoría: **Integration**)
5. Haga clic en **Instalar**
6. Reinicie Home Assistant

</details>

<details>
<summary><b>Manual</b></summary>

1. Copie el directorio `custom_components/owserver/` en su directorio `config/custom_components/` de Home Assistant
2. Reinicie Home Assistant

</details>

---

## ⚙️ Configuración

1. Vaya a **Configuración → Dispositivos y servicios**
2. Haga clic en **Agregar integración**
3. Busque **OW-SERVER (EDS)**
4. Ingrese los datos de su OW-SERVER:

| Parámetro | Predeterminado | Descripción |
|-----------|----------------|-------------|
| **Host** | – | Dirección IP o nombre de host |
| **Puerto** | `80` | Puerto HTTP |
| **Usuario** | `admin` | Nombre de usuario |
| **Contraseña** | `eds` | Contraseña |

---

## 🔌 Sensores Compatibles

| Familia | Tipo | Mediciones |
|---------|------|------------|
| DS18B20 | 🌡️ Sensor de temperatura | Temperatura |
| DS18S20 | 🌡️ Sensor de temperatura | Temperatura |
| DS1822 | 🌡️ Sensor de temperatura | Temperatura |
| EDS0064 | 🌡️ Sensor de temperatura | Temperatura |
| EDS0065 | 🌡️💧 Temp + Humedad | Temperatura, Humedad |
| EDS0066 | 🌡️📊 Temp + Presión | Temperatura, Presión |
| EDS0067 | 🌡️☀️ Temp + Luz | Temperatura, Luz |
| EDS0068 | 🌡️💧📊☀️ Temp + Humedad + Presión + Luz | Temperatura, Humedad, Presión, Luz |
| EDS0071/0072 | 🌡️ Temperatura RTD | Temperatura |

---

## 📁 Estructura del Repositorio

```
custom_components/owserver/
├── __init__.py       # Configuración de la integración
├── config_flow.py    # Interfaz de configuración
├── const.py          # Constantes
├── coordinator.py    # Coordinador de actualización de datos
├── diagnostics.py    # Soporte de diagnóstico
├── manifest.json     # Manifiesto de integración
├── sensor.py         # Plataforma de sensores
├── services.yaml     # Definiciones de servicios
└── strings.json      # Traducciones
```

---

## 📄 Licencia

MIT
