from autoreferral import AutoReferral

referral_link = str(input("Ссылка на ваш реферальный код: "))

while True:
    try:
        number_of_registrations = int(input("Сколько добавить монеток? (1 аккаунт = 5 монеток): "))
        if number_of_registrations <= 0:
            print(f"Алё, я не могу зарегать {number_of_registrations} акков")
        else:
            break
    except ValueError:
        print("Вводи число, не буковки")

show_process = False
while True:
    user_input = input("Показывать процесс? y/n: ").lower()
    if user_input == 'n':
        break
    elif user_input == 'y':
        show_process = True
        break
    else:
        print("Выбери y или n (y = да, n = нет)")

referal = AutoReferral(referral_link=referral_link, number_of_registrations=number_of_registrations,
                       show_process=show_process)

referal.start_registration()
