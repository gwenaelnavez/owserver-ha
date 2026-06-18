[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md)

# 🌡️ OW-SERVER (EDS) für Home Assistant

Home Assistant Integration für [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), einen 1-Wire-zu-Ethernet-Server. Erkennt und überwacht automatisch alle angeschlossenen 1-Wire-Sensoren.

---

## ✨ Funktionen

- **🔍 Auto-Erkennung** – Erkennt automatisch alle angeschlossenen 1-Wire-Sensoren
- **🌡️ Multi-Sensor** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Einzelmessungen** – Temperatur, Luftfeuchtigkeit, Druck, Licht als einzelne Entitäten
- **📦 Physische Gruppierung** – Sensoren nach Gerät im Geräteregister gruppiert
- **⏱️ Konfigurierbares Polling** – Standard 30s Intervall
- **🔐 Authentifizierte Verbindungen** – Unterstützt Benutzername/Passwort
- **📄 Duales Format** – Verarbeitet XML- und CSV-Antworten

---

## 📥 Installation

<details>
<summary><b>HACS (empfohlen)</b></summary>

1. Öffnen Sie HACS in Home Assistant
2. Gehen Sie zu **Integrationen**
3. Klicken Sie auf die drei Punkte oben rechts und wählen Sie **Benutzerdefinierte Repositories**
4. Fügen Sie `https://github.com/gwenaelnavez/owserver-ha` als benutzerdefiniertes Repository hinzu (Kategorie: **Integration**)
5. Klicken Sie auf **Installieren**
6. Starten Sie Home Assistant neu

</details>

<details>
<summary><b>Manuell</b></summary>

1. Kopieren Sie das Verzeichnis `custom_components/owserver/` in Ihr `config/custom_components/`-Verzeichnis von Home Assistant
2. Starten Sie Home Assistant neu

</details>

---

## ⚙️ Konfiguration

1. Gehen Sie zu **Einstellungen → Geräte und Dienste**
2. Klicken Sie auf **Integration hinzufügen**
3. Suchen Sie nach **OW-SERVER (EDS)**
4. Geben Sie Ihre OW-SERVER-Daten ein:

| Parameter | Standard | Beschreibung |
|-----------|----------|--------------|
| **Host** | – | IP-Adresse oder Hostname |
| **Port** | `80` | HTTP-Port |
| **Benutzername** | `admin` | Anmeldename |
| **Passwort** | `eds` | Anmeldekennwort |

---

## 🔌 Unterstützte Sensoren

| Familie | Typ | Messwerte |
|---------|-----|-----------|
| DS18B20 | 🌡️ Temperatursensor | Temperatur |
| DS18S20 | 🌡️ Temperatursensor | Temperatur |
| DS1822 | 🌡️ Temperatursensor | Temperatur |
| EDS0064 | 🌡️ Temperatursensor | Temperatur |
| EDS0065 | 🌡️💧 Temperatur + Luftfeuchtigkeit | Temperatur, Luftfeuchtigkeit |
| EDS0066 | 🌡️📊 Temperatur + Druck | Temperatur, Druck |
| EDS0067 | 🌡️☀️ Temperatur + Licht | Temperatur, Licht |
| EDS0068 | 🌡️💧📊☀️ Temperatur + Luftfeuchtigkeit + Druck + Licht | Temperatur, Luftfeuchtigkeit, Druck, Licht |
| EDS0071/0072 | 🌡️ RTD-Temperatur | Temperatur |

---

## 📁 Repository-Struktur

```
custom_components/owserver/
├── __init__.py       # Integrations-Setup
├── config_flow.py    # Konfigurations-UI
├── const.py          # Konstanten
├── coordinator.py    # Datenaktualisierungs-Koordinator
├── diagnostics.py    # Diagnoseunterstützung
├── manifest.json     # Integrations-Manifest
├── sensor.py         # Sensor-Plattform
├── services.yaml     # Dienstdefinitionen
└── strings.json      # Übersetzungen
```

---

## 📄 Lizenz

MIT
