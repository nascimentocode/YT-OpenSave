import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        return {"theme": "light"}

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
           return json.load(file)

def save_settings(settings):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
