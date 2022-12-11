from selenium.webdriver.common.by import By


#локаторы страницы регистрации
class TestLocators:

    NAME_INPUT = By.XPATH, ".// label[text()='Имя']/../input"#поле "имя" на странице регистрации
    EMAIL_INPUT = By.XPATH, ".// label[text()='Email']/../input"#поле "email" на странице регистрации
    PASS_INPUT = By.XPATH, ".// label[text()='Пароль']/../input"# поле "пароль" на странице регистрации
    REGISTER_BUTTON = By.XPATH, ".// button[text()='Зарегистрироваться']"# кнопка "Зарегистрироваться" на странице регистрации
    INCORRECT_PASSWORD = By.XPATH, ".// p[text()='Некорректный пароль']"# элемент с надписью "Некорректный пароль" на странице регистрации

#локаторы страницы "вход"
class TestLocators_login:

    EMAIL_INPUT_LOGIN = By.XPATH, ".// label[text()='Email']/../input" #поле "email" на странице вход (войти в аккаунт)
    PASS_INPUT_LOGIN = By.XPATH, ".// label[text()='Пароль']/../input" #поле "пароль" на странице вход (войти в аккаунт)
    lOG_IN_BUTTON = By.CLASS_NAME, "button_button__33qZ0" #кнопка "войти" на странице вход

#кнопки перехода на страницу " войти"

class TestLocators_buttons_login:
    HOME_PAGE_LOGIN_BUTTON = By.CLASS_NAME, "button_button__33qZ0" #кнопка "войти в аккаунт на стартовой странице
    HOME_PAGE_PERSONAL_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']/.." #кнопка "личный кабинет" на стартовой странице
    HOME_PAGE_CONSTRUCTOT_BUTTON = By.XPATH, ".//p[text()='Конструктор']/.." #кнопка "конструктор" на странице личного кабинета
    REGISTR_LOG_IN_BUTTON =By.CLASS_NAME, "Auth_link__1fOlj" #Кнопка "войти" страница регистрации
    PASSWORD_FORGOT_LOG_IN_BUTTON = By.CLASS_NAME, 'Auth_link__1fOlj' # Кнопка "войти" страница восстановление пароля
    HOME_PAGE_STELLAR_LOGO_BUTTON = By.CLASS_NAME, "AppHeader_header__logo__2D0X2" #Кнопка "stellar burgers"
    PERSONAL_CUB_LOG_OUT_BUTTON = By.XPATH, ".//button[text()='Выход']" # кнопка "выход" в личном кабинете



class TestLocators_tabs:
    BREAD_TAB = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][1]"# вкладка "булки"
    SAUCE_TAB = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][2]" # вкладка "соусы"
    FILLING_TAB = By.XPATH, ".//*[contains(@class, 'tab_tab__1SPyG')][3]" # вкладка "начинки"

