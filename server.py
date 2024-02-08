import threading
from create_mail import create_mail
from time import sleep


# функция для потока (Я В ПОТОКЕ 😈😈😈😈)
def create_and_register():
    regestration_link = 'https://mathgptpro.com?inv=CPH3S'
    create_mail(regestration_link, show_process=True)
    # open('http://127.0.0.1:5000')
    print('Выдал почту')
    print('Вы можете закрыть программу. OwO❤')


print("""Запуск прошел успешно UwU❤
Начинаю регистрацию""")

if __name__ == "__main__":
    for _ in range(10):  # create 10 threads
        t = threading.Thread(target=create_and_register)
        t.start()

