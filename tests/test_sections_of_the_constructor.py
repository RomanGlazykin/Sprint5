from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_check_sauces_section(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    tab_element = wait.until(EC.visibility_of_element_located(SAUCES_TAB))
    driver.execute_script("arguments[0].scrollIntoView();", tab_element)
    driver.execute_script("arguments[0].click();", tab_element)

    header_text_element = wait.until(EC.visibility_of_element_located(SAUCES_HEADER))
    assert header_text_element.text == "Соусы"


def test_check_toppings_section(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    tab_element = wait.until(EC.visibility_of_element_located(FILLINGS_TAB))
    driver.execute_script("arguments[0].scrollIntoView();", tab_element)
    driver.execute_script("arguments[0].click();", tab_element)

    header_text_element = wait.until(EC.visibility_of_element_located(FILLINGS_HEADER))
    assert header_text_element.text == "Начинки"


def test_check_buns_section(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    fillings_tab_element = driver.find_element(*FILLINGS_TAB)
    driver.execute_script("arguments[0].scrollIntoView();", fillings_tab_element)
    fillings_tab_element.click()

    buns_tab_element = driver.find_element(*BUNS_TAB)
    driver.execute_script("arguments[0].scrollIntoView();", buns_tab_element)
    buns_tab_element.click()

    header_text_element = wait.until(EC.visibility_of_element_located(BUNS_HEADER))
    assert header_text_element.text == "Булки"
