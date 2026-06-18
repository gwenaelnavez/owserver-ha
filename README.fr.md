[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md)

# 🌡️ OW-SERVER (EDS) pour Home Assistant

Intégration Home Assistant pour [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), un serveur 1-Wire vers Ethernet. Découvre et surveille automatiquement tous les capteurs 1-Wire connectés.

---

## ✨ Fonctionnalités

- **🔍 Auto-découverte** – Détecte automatiquement tous les capteurs 1-Wire connectés
- **🌡️ Multi-capteurs** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Entités par mesure** – Température, Humidité, Pression, Lumière en capteurs individuels
- **📦 Regroupement physique** – Capteurs groupés par périphérique dans le registre des appareils
- **⏱️ Polling configurable** – Intervalle par défaut de 30s
- **🔐 Connexions authentifiées** – Support identifiant/mot de passe
- **📄 Format dual** – Gère les réponses XML et CSV

---

## 📥 Installation

<details>
<summary><b>HACS (recommandé)</b></summary>

1. Ouvrez HACS dans Home Assistant
2. Allez dans **Intégrations**
3. Cliquez sur les trois points en haut à droite et sélectionnez **Dépôts personnalisés**
4. Ajoutez `https://github.com/gwenaelnavez/owserver-ha` comme dépôt personnalisé (catégorie : **Integration**)
5. Cliquez sur **Installer**
6. Redémarrez Home Assistant

</details>

<details>
<summary><b>Manuel</b></summary>

1. Copiez le dossier `custom_components/owserver/` dans votre dossier `config/custom_components/` de Home Assistant
2. Redémarrez Home Assistant

</details>

---

## ⚙️ Configuration

1. Allez dans **Paramètres → Appareils et services**
2. Cliquez sur **Ajouter une intégration**
3. Recherchez **OW-SERVER (EDS)**
4. Saisissez les informations de votre OW-SERVER :

| Paramètre | Défaut | Description |
|-----------|--------|-------------|
| **Hôte** | – | Adresse IP ou nom d'hôte |
| **Port** | `80` | Port HTTP |
| **Nom d'utilisateur** | `admin` | Identifiant |
| **Mot de passe** | `eds` | Mot de passe |

---

## 🔌 Capteurs Supportés

| Famille | Type | Mesures |
|---------|------|---------|
| DS18B20 | 🌡️ Capteur de température | Température |
| DS18S20 | 🌡️ Capteur de température | Température |
| DS1822 | 🌡️ Capteur de température | Température |
| EDS0064 | 🌡️ Capteur de température | Température |
| EDS0065 | 🌡️💧 Température + Humidité | Température, Humidité |
| EDS0066 | 🌡️📊 Température + Pression | Température, Pression |
| EDS0067 | 🌡️☀️ Température + Lumière | Température, Lumière |
| EDS0068 | 🌡️💧📊☀️ Température + Humidité + Pression + Lumière | Température, Humidité, Pression, Lumière |
| EDS0071/0072 | 🌡️ Température RTD | Température |

---

## 📁 Structure du Dépôt

```
custom_components/owserver/
├── __init__.py       # Configuration de l'intégration
├── config_flow.py    # Interface de configuration
├── const.py          # Constantes
├── coordinator.py    # Coordonnateur de mise à jour
├── diagnostics.py    # Support diagnostic
├── manifest.json     # Manifeste d'intégration
├── sensor.py         # Plateforme capteurs
├── services.yaml     # Définitions de services
└── strings.json      # Traductions
```

---

## 📄 Licence

MIT
