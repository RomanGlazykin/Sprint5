from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

def test_check_toppings_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 20)

    tab_element = wait.until(EC.visibility_of_element_located(FILLINGS_TAB))
    driver.execute_script("arguments[0].scrollIntoView();", tab_element)
    driver.execute_script("arguments[0].click();", tab_element)

    header_text_element = wait.until(EC.visibility_of_element_located(FILLINGS_HEADER))
    assert header_text_element.text == "Начинки"

    driver.quit()