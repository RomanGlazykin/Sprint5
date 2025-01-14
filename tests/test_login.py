from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_login_button_on_main_page(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")

    driver.find_element(*PASSWORD_INPUT).send_keys("123456")

    driver.find_element(*ENTER_BUTTON).click()

    order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
    assert order_button.text == "Оформить заказ"


def test_login_from_password_recovery(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*RESTORE_PASSWORD_LINK).click()
    driver.find_element(*LOGIN_LINK).click()

    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()

    order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
    assert order_button.text == "Оформить заказ"


def test_login_from_registration_form(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*REGISTER_LINK).click()
    driver.find_element(*LOGIN_LINK).click()

    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()

    order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
    assert order_button.text == "Оформить заказ"


def test_login_profile_button(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()

    order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
    assert order_button.text == "Оформить заказ"
