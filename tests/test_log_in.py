from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators_login
from locators import TestLocators_buttons_login
import time





class Testlogin:

    def test_log_in_home_page(self):
        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get('https://stellarburgers.nomoreparties.site/')
        browser.set_window_size(1920, 1080)


    # нажимаем кнопку "Войти в аккаунт" на стартовой странице
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_LOGIN_BUTTON)).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    # логин в систему
        email_field = browser.find_element(*TestLocators_login.EMAIL_INPUT_LOGIN)
        email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
        pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN)
        pas_field.send_keys('123456')
        log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        cur_url_1 = browser.current_url
        browser.quit()
        assert "login" not in cur_url_1

    def test_log_in_with_personal(self):
        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get('https://stellarburgers.nomoreparties.site/')
        browser.set_window_size(1920, 1080)
    #переходим в личный кабинет
        button_personal = WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        email_field = browser.find_element(*TestLocators_login.EMAIL_INPUT_LOGIN)
        email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
        pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN)
        pas_field.send_keys('123456')
        log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        cur_url_2=browser.current_url
        browser.quit()
        assert "login" not in cur_url_2

    def test_log_in_with_register_form(self):
        browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get('https://stellarburgers.nomoreparties.site/register')
        browser.set_window_size(1920, 1080)


    # нажимаем "войти" на странице регистрации
        button_reg_login=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.REGISTR_LOG_IN_BUTTON)).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
    #логин в систему
        email_field = browser.find_element(*TestLocators_login.EMAIL_INPUT_LOGIN)
        email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
        pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN)
        pas_field.send_keys('123456')
        log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        cur_url_3 = browser.current_url
        browser.quit()
        assert "login" not in cur_url_3

    def test_log_in_password_forgot_form(self):
        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get('https://stellarburgers.nomoreparties.site/forgot-password')
        browser.set_window_size(1920, 1080)
    # нажимаем кнопку "войти" в форме восстановления пароля
        forgot_button_login = WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.PASSWORD_FORGOT_LOG_IN_BUTTON)).click()
    #логин в систему
        email_field = browser.find_element(*TestLocators_login.EMAIL_INPUT_LOGIN)
        email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
        pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN)
        pas_field.send_keys('123456')
        log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
        WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        cur_url_4 = browser.current_url
        browser.quit()
        assert "login" not in cur_url_4








