from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_registration_valid(driver, random_email):
    driver.get(BASE_URL)

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


def test_registration_invalid_password(driver, random_email):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()

    name_fields = driver.find_elements(*REGISTRATION_NAME_INPUT)
    name_fields[0].send_keys("roman")
    name_fields[1].send_keys(random_email)

    driver.find_element(*PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*REGISTRATION_BUTTON).click()

    error_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(INCORRECT_PASSWORD_MESSAGE))
    assert error_message.text == "Некорректный пароль"

