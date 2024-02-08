import threading
from create_mail import create_mail


class AutoReferral:
    def __init__(self, referral_link: str, number_of_registrations: int = 1, show_process: bool = False):
        self.referral_link = referral_link
        self.number_of_registrations = number_of_registrations
        self.show_process = show_process

    def create_and_register(self, referral_link, show_process):
        create_mail(referral_link, show_process=show_process)
        print('Выдал почту')
        print('Все готово, можете закрыть программу')

    def start_registration(self):
        for _ in range(self.number_of_registrations):
            t = threading.Thread(target=self.create_and_register, args=(self.referral_link, self.show_process))
            t.start()


if __name__ == "__main__":
    auto_referral = AutoReferral(referral_link="https://mathgptpro.com?inv=PPV4KJ", number_of_registrations=5,
                                 show_process=True)
    auto_referral.start_registration()