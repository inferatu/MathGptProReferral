from time import sleep as wait

from selenium import webdriver
from selenium.webdriver.common.by import By


def process_verification_link(link: str, show_process=False):
    if not show_process:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        options.add_argument('--disable-dev-shm-usage') # чтобы памяти много не жрало
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    driver.get(link)
    wait(12)
    driver.find_element(By.ID, value="input-firstName").clear()
    driver.find_element(By.ID, value="input-firstName").send_keys('asd')
    driver.find_element(By.ID, value="input-lastName").clear()
    driver.find_element(By.ID, value="input-lastName").send_keys('asd')
    driver.find_element(By.CSS_SELECTOR, value=".MuiGrid-root:nth-child(2) > .MuiFormControl-root").click()
    driver.find_element(By.ID, value="input-education-signup").click()
    driver.find_element(By.ID, value="input-education-signup-option-10").click()

    driver.find_element(By.ID, value="input-password-new").send_keys('Password1')
    driver.find_element(By.ID, value="input-password-again").send_keys('Password1')
    driver.find_element(By.CSS_SELECTOR, value=".MuiButton-root").click()
    wait(3)
    driver.quit()
    # exit(0)
