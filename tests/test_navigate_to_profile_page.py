from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_navigate_to_profile_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

    text_change_personal_information = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PROFILE_PAGE_TEXT))
    assert text_change_personal_information.text == "В этом разделе вы можете изменить свои персональные данные"

    driver.quit()