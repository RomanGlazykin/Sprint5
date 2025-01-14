import pytest
import random
import string
from selenium import webdriver


@pytest.fixture
def random_email():
    """Генерирует случайный email в формате login@domain. Например, 123@ya.ru"""
    login_length = random.randint(5, 10)  # Длина логина от 5 до 10 символов
    login = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(login_length))  # Генерация логина

    domains = ["ya.ru", "mail.ru", "gmail.com", "example.com"] #Список доменов
    domain = random.choice(domains) #Выбор домена из списка
    return f"{login}@{domain}"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()