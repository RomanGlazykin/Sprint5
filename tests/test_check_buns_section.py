from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

def test_check_buns_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 20)

    fillings_tab_element = driver.find_element(*FILLINGS_TAB)
    driver.execute_script("arguments[0].scrollIntoView();", fillings_tab_element)
    fillings_tab_element.click()

    buns_tab_element = driver.find_element(*BUNS_TAB)
    driver.execute_script("arguments[0].scrollIntoView();", buns_tab_element)
    buns_tab_element.click()

    header_text_element = wait.until(EC.visibility_of_element_located(BUNS_HEADER))
    assert header_text_element.text == "Булки"

    driver.quit()