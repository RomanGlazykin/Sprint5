from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_registration(random_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()

    name_fields = driver.find_elements(*REGISTRATION_NAME_INPUT)
    name_fields[0].send_keys("roman")
    name_fields[1].send_keys(random_email)

    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ENTER_BUTTON))

    login_page = driver.find_element(*LOGIN_PAGE_HEADER)
    assert login_page.text == 'Вход'

    driver.quit()
