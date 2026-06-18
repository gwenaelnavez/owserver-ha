[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md) | [Italiano](README.it.md)

# 🌡️ OW-SERVER (EDS) per Home Assistant

Integrazione Home Assistant per [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), un server 1-Wire verso Ethernet. Scopre e monitora automaticamente tutti i sensori 1-Wire collegati.

---

## ✨ Caratteristiche

- **🔍 Auto-scoperta** – Rileva automaticamente tutti i sensori 1-Wire collegati
- **🌡️ Multi-sensore** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Entità per misurazione** – Temperatura, Umidità, Pressione, Luce come sensori individuali
- **📦 Raggruppamento fisico** – Sensori raggruppati per dispositivo nel registro dei dispositivi
- **⏱️ Polling configurabile** – Intervallo predefinito di 30s
- **🔐 Connessioni autenticate** – Supporta login con utente/password
- **📄 Formato duale** – Gestisce risposte XML e CSV

---

## 📥 Installazione

<details>
<summary><b>HACS (consigliato)</b></summary>

1. Apri HACS in Home Assistant
2. Vai a **Integrazioni**
3. Clicca sui tre punti in alto a destra e seleziona **Repository personalizzati**
4. Aggiungi `https://github.com/gwenaelnavez/owserver-ha` come repository personalizzato (categoria: **Integration**)
5. Clicca su **Installa**
6. Riavvia Home Assistant

</details>

<details>
<summary><b>Manuale</b></summary>

1. Copia la directory `custom_components/owserver/` nella directory `config/custom_components/` del tuo Home Assistant
2. Riavvia Home Assistant

</details>

---

## ⚙️ Configurazione

1. Vai a **Impostazioni → Dispositivi e servizi**
2. Clicca su **Aggiungi integrazione**
3. Cerca **OW-SERVER (EDS)**
4. Inserisci i dati del tuo OW-SERVER:

| Parametro | Predefinito | Descrizione |
|-----------|-------------|-------------|
| **Host** | – | Indirizzo IP o nome host |
| **Porta** | `80` | Porta HTTP |
| **Utente** | `admin` | Nome utente |
| **Password** | `eds` | Password di accesso |

---

## 🔌 Sensori Supportati

| Famiglia | Tipo | Misurazioni |
|----------|------|-------------|
| DS18B20 | 🌡️ Sensore di temperatura | Temperatura |
| DS18S20 | 🌡️ Sensore di temperatura | Temperatura |
| DS1822 | 🌡️ Sensore di temperatura | Temperatura |
| EDS0064 | 🌡️ Sensore di temperatura | Temperatura |
| EDS0065 | 🌡️💧 Temp + Umidità | Temperatura, Umidità |
| EDS0066 | 🌡️📊 Temp + Pressione | Temperatura, Pressione |
| EDS0067 | 🌡️☀️ Temp + Luce | Temperatura, Luce |
| EDS0068 | 🌡️💧📊☀️ Temp + Umidità + Pressione + Luce | Temperatura, Umidità, Pressione, Luce |
| EDS0071/0072 | 🌡️ Temperatura RTD | Temperatura |

---

## 📁 Struttura del Repository

```
custom_components/owserver/
├── __init__.py       # Configurazione dell'integrazione
├── config_flow.py    # Interfaccia di configurazione
├── const.py          # Costanti
├── coordinator.py    # Coordinatore aggiornamenti
├── diagnostics.py    # Supporto diagnostica
├── manifest.json     # Manifesto dell'integrazione
├── sensor.py         # Piattaforma sensori
├── services.yaml     # Definizioni servizi
└── strings.json      # Traduzioni
```

---

## 📄 Licenza

MIT
