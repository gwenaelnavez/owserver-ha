# OW-SERVER (EDS) pour Home Assistant

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md)

Intégration Home Assistant pour [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), un serveur 1-Wire vers Ethernet.

## Fonctionnalités

- Découvre automatiquement tous les capteurs 1-Wire connectés
- Supporte DS18B20, DS18S20, DS1822, DS2438, et les capteurs EDS (EDS0064, EDS0065, EDS0066, EDS0067, EDS0068, etc.)
- Crée des entités individuelles pour chaque mesure (Température, Humidité, Pression, Lumière)
- Regroupe les capteurs par périphérique physique dans le registre des appareils
- Intervalle de polling configurable (défaut : 30s)
- Supporte les connexions authentifiées
- Gère les formats XML et CSV

## Installation

### HACS (recommandé)

1. Ouvrez HACS dans Home Assistant
2. Allez dans **Intégrations**
3. Cliquez sur les trois points en haut à droite et sélectionnez **Dépôts personnalisés**
4. Ajoutez `https://github.com/gwenaelnavez/owserver-ha` comme dépôt personnalisé (catégorie : Integration)
5. Cliquez sur **Installer**
6. Redémarrez Home Assistant

### Manuel

1. Copiez le dossier `custom_components/owserver/` dans votre dossier `config/custom_components/` de Home Assistant
2. Redémarrez Home Assistant

## Configuration

1. Allez dans **Paramètres → Appareils et services**
2. Cliquez sur **Ajouter une intégration**
3. Recherchez **OW-SERVER (EDS)**
4. Saisissez les informations de votre OW-SERVER :
   - **Hôte** : Adresse IP ou nom d'hôte
   - **Port** : 80 (par défaut)
   - **Nom d'utilisateur** : admin (par défaut)
   - **Mot de passe** : eds (par défaut)

## Capteurs Supportés

| Famille | Type | Mesures |
|---------|------|---------|
| DS18B20 | Capteur de température | Température |
| DS18S20 | Capteur de température | Température |
| DS1822 | Capteur de température | Température |
| EDS0064 | Capteur de température | Température |
| EDS0065 | Température + Humidité | Température, Humidité |
| EDS0066 | Température + Pression | Température, Pression |
| EDS0067 | Température + Lumière | Température, Lumière |
| EDS0068 | Température + Humidité + Pression + Lumière | Température, Humidité, Pression, Lumière |
| EDS0071/0072 | Température RTD | Température |

## Licence

MIT
