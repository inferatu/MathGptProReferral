from autoreferral import AutoReferral
from settings import *

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
