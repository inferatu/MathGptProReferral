from autoreferral import AutoReferral


referall_link = str(input("Ссылка на ваш реферальный код: "))
number_of_regestrations = int(input("Сколько добавить монеток? (1 аккаунт = 5 монеток): "))

if input("Показывать процесс? y/n: ").lower() == 'y':
    show_process = True
else:
    show_process = False

referal = AutoReferral(referral_link=referall_link, number_of_registrations=number_of_regestrations,
                       show_process=show_process)

referal.start_registration()