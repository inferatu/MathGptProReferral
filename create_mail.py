import re
from time import sleep as wait
from pytempmail import TempMail
from selenium import webdriver
from selenium.webdriver.common.by import By

from register_user import process_verification_link


def create_mail(link, show_process=False):
    tm = TempMail()

    # Вывести на экран текущую почту
    print(f'Email: {tm.email}')

    printed_mails = []
    opened_link = False  # обязательно чтобы не переходить по ссылке мильон раз
    if not show_process:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        options.add_argument('--disable-dev-shm-usage')  # чтобы памяти много не жрало
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    driver.get(link)
    wait(3)
    driver.find_element(By.ID, value="input-email").send_keys(tm.email)
    driver.find_element(By.CSS_SELECTOR, value=".MuiButton-contained").click()
    wait(5)
    driver.quit()

    try:
        while True:
            all_mails = tm.get_mails()
            for mail in all_mails:
                if mail.id not in printed_mails:
                    printed_mails.append(mail.id)

                    print(f'Body: {mail.text}')
                    print('\n-  -  -  -  -  END  -  -  -  -  -\n')

                    # проверка на ссылку
                    url_pattern = r'\[https://mathgptpro\.com/login/verification/\S+\]'
                    urls = re.findall(url_pattern, mail.text)

                    # убираем [] чтобы нормальная ссылка была
                    cleaned_urls = [url.strip('[]') for url in urls]

                    if cleaned_urls and not opened_link:
                        # [0] для первой ссылки в почте
                        if not show_process:
                            process_verification_link(cleaned_urls[0], show_process=False)
                        else:
                            process_verification_link(cleaned_urls[0], show_process=True)
                        # opened_link = True  # ставим правду
                        break
                break
            # wait(5)
            break
        return tm.email
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
