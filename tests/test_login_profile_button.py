from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

def test_login_profile_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()

    order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(ORDER_BUTTON))
    assert order_button.text == "Оформить заказ"

    driver.quit()