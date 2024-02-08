import json
import os
from autoreferral import AutoReferral

SETTINGS_FILE = 'settings.json'


def create_settings_file():
    # TODO: move that function to other file
    referral_link = input("Ссылка на ваш реферальный код: ")

    show_process = None
    while show_process not in ['y', 'n']:
        show_process = input("Показывать процесс? y/n: ").lower()
        if show_process not in ['y', 'n']:
            print("Нужно ввести y или n")

    settings = {
        "referral_link": referral_link,
        "show_process": True if show_process == 'y' else False
    }

    try:
        with open(SETTINGS_FILE, 'w', encoding='utf8') as f:
            json.dump(settings, f)
    except Exception as e:
        print(f'Возникла ошибка при создании файла: {e}')


def load_settings():
    # TODO: move that function to other file
    if not os.path.exists(SETTINGS_FILE):
        print("Файл настроек не найден. Давайте его создадим.")
        create_settings_file()

    try:
        with open(SETTINGS_FILE, 'r', encoding='utf8') as f:
            settings = json.load(f)
        return settings
    except Exception as e:
        print(f"Ошибка при загрузке настроек: {e}")
        return None


settings = load_settings()

while True:
    try:
        number_of_registrations = int(input("Сколько добавить монеток? (1 аккаунт = 5 монеток): "))
        if number_of_registrations > 10:
            if input("Количество аккаунтов больше 10 может работать некорректно. Хотите продолжить? y/n: ") == 'y':
                pass
            else:
                print(f'Регестрирую 10 аккаунтов вместо: {number_of_registrations}')

                number_of_registrations = 1
        break
    except ValueError:
        print("Нужно число, не слова")

if settings is not None:
    referral = AutoReferral(referral_link=settings['referral_link'],
                            number_of_registrations=number_of_registrations,
                            show_process=settings['show_process'])

    referral.start_registration()
    print("Программа закроется, когда все будет готово")

else:
    print("Не могу получить доступ к настройкам. Убедись что у меня есть права")
