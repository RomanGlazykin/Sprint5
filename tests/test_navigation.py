from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_logo_click_navigation(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*LOGO_LINK).click()

    text_assemble_the_burger = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MAIN_PAGE_HEADER))
    assert text_assemble_the_burger.text == "Соберите бургер"


def test_navigate_to_profile_page(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

    text_change_personal_information = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PROFILE_PAGE_TEXT))
    assert text_change_personal_information.text == "В этом разделе вы можете изменить свои персональные данные"


def test_profile_to_constructor_navigation(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*CONSTRUCTOR_LINK).click()

    text_assemble_the_burger = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MAIN_PAGE_HEADER))
    assert text_assemble_the_burger.text == "Соберите бургер"
