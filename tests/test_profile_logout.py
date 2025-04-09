from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_profile_logout(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
    driver.find_element(*LOGOUT_BUTTON).click()

    login_page = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LOGIN_PAGE_HEADER))
    assert login_page.text == "Вход"
