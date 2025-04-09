from selenium.webdriver.common.by import By

# Главная страница
FILLINGS_TAB = (By.XPATH, "//div[span[text()='Начинки']]")  # Вкладка "Начинки"
BUNS_TAB = (By.XPATH, "//div[span[text()='Булки']]")       # Вкладка "Булки"
BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")          # Заголовок раздела "Булки"
SAUCES_TAB = (By.XPATH, "//div[span[text()='Соусы']]") # Вкладка "Соусы"
SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']") # Заголовок раздела "Соусы"
FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']") # Заголовок раздела "Начинки"
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
EMAIL_INPUT = (By.NAME, "name") # Поле ввода email
PASSWORD_INPUT = (By.NAME, "Пароль") # Поле ввода пароля
ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" в форме
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Ссылка "Личный Кабинет"
RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']") # Ссылка "Восстановить пароль"
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Ссылка "Войти"
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']") # Ссылка "Зарегистрироваться"
LOGO_LINK = (By.CSS_SELECTOR, '#root > div > header > nav > div > a')  # Логотип
MAIN_PAGE_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # Заголовок страницы "Соберите бургер"
PROFILE_PAGE_TEXT = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']") # Текст на странице профиля
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход"
LOGIN_PAGE_HEADER = (By.XPATH, "//h2") # Заголовок страницы входа
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # Ссылка "Конструктор"
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
REGISTRATION_NAME_INPUT = (By.NAME, "name") # Поле ввода имени при регистрации
INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение о некорректном пароле