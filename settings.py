import json
import os

SETTINGS_FILE = 'settings.json'


def create_settings_file():
    referral_link = input("Your referral link: ")

    show_process = None
    while show_process not in ['y', 'n']:
        show_process = input("Show process? y/n: ").lower()
        if show_process not in ['y', 'n']:
            print("You must enter either 'y' or 'n'.")

    settings = {
        "referral_link": referral_link,
        "show_process": True if show_process == 'y' else False
    }

    try:
        with open(SETTINGS_FILE, 'w', encoding='utf8') as f:
            json.dump(settings, f)
    except Exception as e:
        print(f'This error appeared when creating file: {e}')


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        print("Options file does not exist, let's create it.")
        create_settings_file()

    try:
        with open(SETTINGS_FILE, 'r', encoding='utf8') as f:
            settings = json.load(f)
        return settings
    except Exception as e:
        print(f"This error appeared while loading file: {e}")
        return None

