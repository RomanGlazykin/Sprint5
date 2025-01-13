from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

def test_registration_invalid_password(random_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()

    name_fields = driver.find_elements(*REGISTRATION_NAME_INPUT)
    name_fields[0].send_keys("roman")
    name_fields[1].send_keys(random_email)

    driver.find_element(*PASSWORD_INPUT).send_keys("1234")
    driver.find_element(*REGISTRATION_BUTTON).click()

    error_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(INCORRECT_PASSWORD_MESSAGE))
    assert error_message.text == "Некорректный пароль"

    driver.quit()
