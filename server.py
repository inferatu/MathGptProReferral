# from threading import Thread
# from flask import Flask, render_template_string
import simpleaudio as sa
# from webbrowser import open
# from waitress import serve
from create_mail import create_mail

# app = Flask(__name__)
my_mail = None


def play_sound(file_name):
    wave_obj = sa.WaveObject.from_wave_file(file_name)
    play_obj = wave_obj.play()
    play_obj.wait_done()


# функция для потока (Я В ПОТОКЕ 😈😈😈😈)
def create_and_register():
    global my_mail
    regestration_link = 'https://mathgptpro.com/new'
    my_mail = create_mail(regestration_link, show_process=True)
    # open('http://127.0.0.1:5000')
    print('Выдал почту')
    play_sound('pop.wav')
    print('Вы можете закрыть программу. OwO❤')


# @app.route('/')
# def home():
#     if my_mail is None:
#         return "Регистрация еще не завершена. Пожалуйста, подождите..."
#     else:
#         password = "Password1"
#         return render_template_string('''
#             <html>
#                 <head>
#                     <style>
#                         button {
#                             --c:  #229091; /* the color*/
#                             box-shadow: 0 0 0 .1em inset var(--c);
#                             --_g: linear-gradient(var(--c) 0 0) no-repeat;
#                             background:
#                                 var(--_g) calc(var(--_p,0%) - 100%) 0%,
#                                 var(--_g) calc(200% - var(--_p,0%)) 0%,
#                                 var(--_g) calc(var(--_p,0%) - 100%) 100%,
#                                 var(--_g) calc(200% - var(--_p,0%)) 100%;
#                             background-size: 50.5% calc(var(--_p,0%)/2 + .5%);
#                             outline-offset: .1em;
#                             transition: background-size .4s, background-position 0s .4s;
#                             font-size: 1rem; /* make buttons smaller */
#                         }
#                         button:hover {
#                             --_p: 100%;
#                             transition: background-position .4s, background-size 0s;
#                         }
#                         button:active {
#                             box-shadow: 0 0 9e9q inset #0009;
#                             background-color: var(--c);
#                             color: #fff;
#                         }
#                         body {
#                             height: 100vh;
#                             margin: 0;
#                             display: flex;
#                             flex-direction: column; /* stack fields vertically */
#                             align-items: flex-start;
#                             justify-content: flex-start;
#                             padding: 20px;
#                             background: #FFFFFF; /* change background color to white */
#                         }
#                         button {
#                             font-family: system-ui, sans-serif;
#                             cursor: pointer;
#                             padding: .1em .6em;
#                             font-weight: bold;
#                             border: none;
#                         }
#                     </style>
#                 </head>
#                 <body>
#                     <p>Login: {{my_mail}} <button onclick="navigator.clipboard.writeText('{{my_mail}}')">Copy</button></p>
#                     <p>Password: {{password}} <button onclick="navigator.clipboard.writeText('{{password}}')">Copy</button></p>
#                 </body>
#             </html>
#         ''', my_mail=my_mail, password=password)
#
#
# def run_app():
#     Thread(target=create_and_register).start()
#     serve(app, host='127.0.0.1', port=5000)
#
#
# if __name__ == '__main__':
#     serve(app, host='127.0.0.1', port=5000)

print("""Запуск прошел успешно UwU❤
Начинаю регистрацию""")


if __name__ == "__main__":
    create_and_register()