[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md) | [Italiano](README.it.md)

# 🌡️ OW-SERVER (EDS) voor Home Assistant

Home Assistant-integratie voor [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), een 1-Wire-naar-Ethernet-server. Ontdekt en bewaakt automatisch alle aangesloten 1-Wire-sensoren.

---

## ✨ Functies

- **🔍 Auto-ontdekking** – Detecteert automatisch alle aangesloten 1-Wire-sensoren
- **🌡️ Multi-sensor** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Per-meting entiteiten** – Temperatuur, Vochtigheid, Druk, Licht als afzonderlijke sensoren
- **📦 Fysieke groepering** – Sensoren gegroepeerd per apparaat in het apparaatregister
- **⏱️ Configureerbaar pollen** – Standaard interval van 30s
- **🔐 Geverifieerde verbindingen** – Ondersteunt gebruikersnaam/wachtwoord
- **📄 Dual formaat** – Verwerkt zowel XML- als CSV-antwoorden

---

## 📥 Installatie

<details>
<summary><b>HACS (aanbevolen)</b></summary>

1. Open HACS in Home Assistant
2. Ga naar **Integraties**
3. Klik op de drie puntjes rechtsboven en selecteer **Aangepaste repositories**
4. Voeg `https://github.com/gwenaelnavez/owserver-ha` toe als aangepaste repository (categorie: **Integration**)
5. Klik op **Installeren**
6. Herstart Home Assistant

</details>

<details>
<summary><b>Handmatig</b></summary>

1. Kopieer de map `custom_components/owserver/` naar uw `config/custom_components/` map van Home Assistant
2. Herstart Home Assistant

</details>

---

## ⚙️ Configuratie

1. Ga naar **Instellingen → Apparaten en services**
2. Klik op **Integratie toevoegen**
3. Zoek naar **OW-SERVER (EDS)**
4. Voer uw OW-SERVER-gegevens in:

| Parameter | Standaard | Beschrijving |
|-----------|-----------|--------------|
| **Host** | – | IP-adres of hostnaam |
| **Poort** | `80` | HTTP-poort |
| **Gebruikersnaam** | `admin` | Inlognaam |
| **Wachtwoord** | `eds` | Inlogwachtwoord |

---

## 🔌 Ondersteunde Sensoren

| Familie | Type | Metingen |
|---------|------|----------|
| DS18B20 | 🌡️ Temperatuursensor | Temperatuur |
| DS18S20 | 🌡️ Temperatuursensor | Temperatuur |
| DS1822 | 🌡️ Temperatuursensor | Temperatuur |
| EDS0064 | 🌡️ Temperatuursensor | Temperatuur |
| EDS0065 | 🌡️💧 Temp + Vochtigheid | Temperatuur, Vochtigheid |
| EDS0066 | 🌡️📊 Temp + Druk | Temperatuur, Druk |
| EDS0067 | 🌡️☀️ Temp + Licht | Temperatuur, Licht |
| EDS0068 | 🌡️💧📊☀️ Temp + Vochtigheid + Druk + Licht | Temperatuur, Vochtigheid, Druk, Licht |
| EDS0071/0072 | 🌡️ RTD-temperatuur | Temperatuur |

---

## 📁 Repository-structuur

```
custom_components/owserver/
├── __init__.py       # Integratie-setup
├── config_flow.py    # Configuratie-UI
├── const.py          # Constanten
├── coordinator.py    # Gegevensupdate-coördinator
├── diagnostics.py    # Diagnose-ondersteuning
├── manifest.json     # Integratie-manifest
├── sensor.py         # Sensor-platform
├── services.yaml     # Service-definities
└── strings.json      # Vertalingen
```

---

## 📄 Licentie

MIT
