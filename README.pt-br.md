[![GitHub Release](https://img.shields.io/github/v/release/gwenaelnavez/owserver-ha?style=for-the-badge)](https://github.com/gwenaelnavez/owserver-ha/releases)
[![HACS Action](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hacs-action.yml)
[![Hassfest](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml/badge.svg)](https://github.com/gwenaelnavez/owserver-ha/actions/workflows/hassfest.yml)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-OS%2017.3+-blue?style=for-the-badge)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/gwenaelnavez/owserver-ha?style=for-the-badge)](LICENSE)

---

[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Nederlands](README.nl.md) | [Português (Brasil)](README.pt-br.md)

# 🌡️ OW-SERVER (EDS) para Home Assistant

Integração do Home Assistant para [EDS OW-SERVER](https://www.embeddeddatasystems.com/OW-SERVER--1-Wire-to-Ethernet-Server_p_152.html), um servidor 1-Wire para Ethernet. Descobre e monitora automaticamente todos os sensores 1-Wire conectados.

---

## ✨ Funcionalidades

- **🔍 Descoberta automática** – Detecta automaticamente todos os sensores 1-Wire conectados
- **🌡️ Multi-sensor** – DS18B20, DS18S20, DS1822, DS2438, EDS0064–EDS0068, EDS0071/0072
- **📊 Entidades por medição** – Temperatura, Umidade, Pressão, Luz como sensores individuais
- **📦 Agrupamento físico** – Sensores agrupados por dispositivo no registro de dispositivos
- **⏱️ Polling configurável** – Intervalo padrão de 30s
- **🔐 Conexões autenticadas** – Suporte a login com usuário/senha
- **📄 Formato duplo** – Processa respostas XML e CSV

---

## 📥 Instalação

<details>
<summary><b>HACS (recomendado)</b></summary>

1. Abra o HACS no Home Assistant
2. Vá para **Integrações**
3. Clique nos três pontos no canto superior direito e selecione **Repositórios personalizados**
4. Adicione `https://github.com/gwenaelnavez/owserver-ha` como repositório personalizado (categoria: **Integration**)
5. Clique em **Instalar**
6. Reinicie o Home Assistant

</details>

<details>
<summary><b>Manual</b></summary>

1. Copie o diretório `custom_components/owserver/` para o diretório `config/custom_components/` do seu Home Assistant
2. Reinicie o Home Assistant

</details>

---

## ⚙️ Configuração

1. Vá para **Configurações → Dispositivos e serviços**
2. Clique em **Adicionar integração**
3. Pesquise por **OW-SERVER (EDS)**
4. Insira os dados do seu OW-SERVER:

| Parâmetro | Padrão | Descrição |
|-----------|--------|-----------|
| **Host** | – | Endereço IP ou nome do host |
| **Porta** | `80` | Porta HTTP |
| **Usuário** | `admin` | Nome de usuário |
| **Senha** | `eds` | Senha de login |

---

## 🔌 Sensores Compatíveis

| Família | Tipo | Medições |
|---------|------|----------|
| DS18B20 | 🌡️ Sensor de temperatura | Temperatura |
| DS18S20 | 🌡️ Sensor de temperatura | Temperatura |
| DS1822 | 🌡️ Sensor de temperatura | Temperatura |
| EDS0064 | 🌡️ Sensor de temperatura | Temperatura |
| EDS0065 | 🌡️💧 Temp + Umidade | Temperatura, Umidade |
| EDS0066 | 🌡️📊 Temp + Pressão | Temperatura, Pressão |
| EDS0067 | 🌡️☀️ Temp + Luz | Temperatura, Luz |
| EDS0068 | 🌡️💧📊☀️ Temp + Umidade + Pressão + Luz | Temperatura, Umidade, Pressão, Luz |
| EDS0071/0072 | 🌡️ Temperatura RTD | Temperatura |

---

## 📁 Estrutura do Repositório

```
custom_components/owserver/
├── __init__.py       # Configuração da integração
├── config_flow.py    # Interface de configuração
├── const.py          # Constantes
├── coordinator.py    # Coordenador de atualização de dados
├── diagnostics.py    # Suporte a diagnóstico
├── manifest.json     # Manifesto da integração
├── sensor.py         # Plataforma de sensores
├── services.yaml     # Definições de serviços
└── strings.json      # Traduções
```

---

## 📄 Licença

MIT
