import re
from time import sleep as wait
from pytempmail import TempMail
from selenium import webdriver
from selenium.webdriver.common.by import By

from register_user import process_verification_link


def create_mail(link, show_process=False):
    tm = TempMail()

    # Prints email on screen
    print(f'Email: {tm.email}')

    printed_mails = []
    opened_link = False  # will change to true so won't be caught in a loop
    if not show_process:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        options.add_argument('--disable-dev-shm-usage')  # wont take much CPU
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    driver.get(link)
    wait(10)
    driver.find_element(By.CSS_SELECTOR, value=".css-splr7f").click()
    driver.find_element(By.ID, value="input-email").send_keys(tm.email)
    driver.find_element(By.CSS_SELECTOR, value=".MuiButton-contained").click()
    wait(10)
    driver.quit()

    try:
        while True:
            all_mails = tm.get_mails()
            for mail in all_mails:
                if mail.id not in printed_mails:
                    printed_mails.append(mail.id)

                    print(f'Body: {mail.text}')
                    print('\n-  -  -  -  -  END  -  -  -  -  -\n')

                    # finding links
                    url_pattern = r'\[https://mathgptpro\.com/login/verification/\S+\]'
                    urls = re.findall(url_pattern, mail.text)

                    # removing [] from a list
                    cleaned_urls = [url.strip('[]') for url in urls]

                    if cleaned_urls and not opened_link:
                        # [0] for first link
                        if not show_process:
                            process_verification_link(cleaned_urls[0], show_process=False)
                        else:
                            process_verification_link(cleaned_urls[0], show_process=True)
                        # opened_link = True  # need to remove too
                        break
                break
            # wait(5)
            break

    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
