import json
import os

if os.name == 'nt':
    BASE_DIR = os.path.join(os.getenv('APPDATA'), "YT-OpenSave")
else:
    BASE_DIR = os.path.join(os.path.expanduser("~"), ".config", "YT-OpenSave")

os.makedirs(BASE_DIR, exist_ok=True)

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

DEFAULT_DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

DEFAULT_SETTINGS = {
    "theme": "light",
    "download_path": DEFAULT_DOWNLOAD_PATH
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_SETTINGS

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
           return json.load(file)

def save_settings(settings):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
