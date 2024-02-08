import json
import os
from autoreferral import AutoReferral

SETTINGS_FILE = 'settings.json'


def create_settings_file():
    # TODO: move that function to other file
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
    # TODO: move that function to other file
    if not os.path.exists(SETTINGS_FILE):
        print("Options file does not exist, let's create him.")
        create_settings_file()

    try:
        with open(SETTINGS_FILE, 'r', encoding='utf8') as f:
            settings = json.load(f)
        return settings
    except Exception as e:
        print(f"This error appeared while loading file: {e}")
        return None


settings = load_settings()

while True:
    try:
        number_of_registrations = int(input("How much coins you need (1 account = 5 coins)?: "))
        if number_of_registrations > 10:
            if input("Using more than 10 accounts may create some errors, proceed? y/n: ") == 'y':
                pass
            else:
                print(f'Registering 10 accounts, not: {number_of_registrations}')

                number_of_registrations = 1
        break
    except ValueError:
        print("You must enter a number, not a string.")

if settings is not None:
    referral = AutoReferral(referral_link=settings['referral_link'],
                            number_of_registrations=number_of_registrations,
                            show_process=settings['show_process'])

    referral.start_registration()
    print("Program will close when everything is done.")

else:
    print("Can't access options file. Are you sure I have all rights?")
