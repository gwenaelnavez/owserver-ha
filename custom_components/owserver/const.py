DOMAIN = "owserver"

CONF_HOST = "host"
CONF_PORT = "port"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_POLL_INTERVAL = "poll_interval"

DEFAULT_PORT = 80
DEFAULT_POLL_INTERVAL = 30
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "eds"

DETAILS_XML_PATH = "/details.xml"

MIN_POLL_INTERVAL = 10

SENSOR_TYPES = {
    "Temperature": {"device_class": "temperature", "unit": "°C", "icon": "mdi:thermometer"},
    "Humidity": {"device_class": "humidity", "unit": "%", "icon": "mdi:water-percent"},
    "Pressure": {"device_class": "pressure", "unit": "mbar", "icon": "mdi:gauge"},
    "Light": {"device_class": "illuminance", "unit": "lx", "icon": "mdi:brightness-5"},
    "DewPoint": {"device_class": "temperature", "unit": "°C", "icon": "mdi:thermometer-water"},
    "HeatIndex": {"device_class": "temperature", "unit": "°C", "icon": "mdi:thermometer"},
    "PrimaryValue": {"device_class": "temperature", "unit": "°C", "icon": "mdi:thermometer"},
}

DEFAULT_SCAN_INTERVAL = 30
