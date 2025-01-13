from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_profile_to_constructor_navigation():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys("qweee@mail.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*ENTER_BUTTON).click()
    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*CONSTRUCTOR_LINK).click()

    text_assemble_the_burger = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MAIN_PAGE_HEADER))
    assert text_assemble_the_burger.text == "Соберите бургер"

    driver.quit()