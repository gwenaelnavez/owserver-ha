# OW-SERVER (EDS) für Home Assistant

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md)

Home Assistant Integration für [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), einen 1-Wire-zu-Ethernet-Server.

## Funktionen

- Erkennt automatisch alle angeschlossenen 1-Wire-Sensoren
- Unterstützt DS18B20, DS18S20, DS1822, DS2438 und EDS-Sensoren (EDS0064, EDS0065, EDS0066, EDS0067, EDS0068, usw.)
- Erstellt einzelne Sensor-Entitäten für jede Messung (Temperatur, Luftfeuchtigkeit, Druck, Licht)
- Gruppiert Sensoren nach physischem Gerät im Geräteregister
- Konfigurierbares Polling-Intervall (Standard: 30s)
- Unterstützt authentifizierte Verbindungen
- Verarbeitet sowohl XML- als auch CSV-Formate

## Installation

### HACS (empfohlen)

1. Öffnen Sie HACS in Home Assistant
2. Gehen Sie zu **Integrationen**
3. Klicken Sie auf die drei Punkte oben rechts und wählen Sie **Benutzerdefinierte Repositories**
4. Fügen Sie `https://github.com/gwenaelnavez/owserver-ha` als benutzerdefiniertes Repository hinzu (Kategorie: Integration)
5. Klicken Sie auf **Installieren**
6. Starten Sie Home Assistant neu

### Manuell

1. Kopieren Sie das Verzeichnis `custom_components/owserver/` in Ihr `config/custom_components/`-Verzeichnis von Home Assistant
2. Starten Sie Home Assistant neu

## Konfiguration

1. Gehen Sie zu **Einstellungen → Geräte und Dienste**
2. Klicken Sie auf **Integration hinzufügen**
3. Suchen Sie nach **OW-SERVER (EDS)**
4. Geben Sie Ihre OW-SERVER-Daten ein:
   - **Host**: IP-Adresse oder Hostname
   - **Port**: 80 (Standard)
   - **Benutzername**: admin (Standard)
   - **Passwort**: eds (Standard)

## Unterstützte Sensoren

| Familie | Typ | Messwerte |
|---------|-----|-----------|
| DS18B20 | Temperatursensor | Temperatur |
| DS18S20 | Temperatursensor | Temperatur |
| DS1822 | Temperatursensor | Temperatur |
| EDS0064 | Temperatursensor | Temperatur |
| EDS0065 | Temperatur + Luftfeuchtigkeit | Temperatur, Luftfeuchtigkeit |
| EDS0066 | Temperatur + Druck | Temperatur, Druck |
| EDS0067 | Temperatur + Licht | Temperatur, Licht |
| EDS0068 | Temperatur + Luftfeuchtigkeit + Druck + Licht | Temperatur, Luftfeuchtigkeit, Druck, Licht |
| EDS0071/0072 | RTD-Temperatur | Temperatur |

## Lizenz

MIT
