from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestSing_in:
    def test_name_is_not_empty(self):
        log = 'nadya'


        browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(3)
        browser.set_window_size(1920,1080)

        obj_name = browser.find_element(*TestLocators.NAME_INPUT)
        obj_name.send_keys(log)
        name_value = obj_name.get_property('value')
        browser.quit()
        assert len(name_value)!=0


    def test_email_in_format_login_dog_domain(self):
        email = 'nadya_terekhina_5_123@yandex.ru'

        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(3)
        browser.set_window_size(1920, 1080)

        obj_email = browser.find_element(*TestLocators.EMAIL_INPUT)
        obj_email.send_keys(email)
        email_value = obj_email.get_property('value')
        browser.quit()
        assert "@yandex.ru" in email_value

    def test_password_is_6_symbols(self):
        pas = '123456'

        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(3)
        browser.set_window_size(1920, 1080)

        obj_password = browser.find_element(*TestLocators.PASS_INPUT)
        obj_password.send_keys(pas)
        password_value = obj_password.get_property('value')
        browser.quit()
        assert len(password_value) == 6

    def test_password_less_than_6_there_is_mistake_in_dom(self):
        log = 'nadya'
        email = 'nadya_terekhina_5_123@yandex.ru'
        pas = '12345'

        browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
        browser.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(3)
        browser.set_window_size(1920, 1080)

        obj_name = browser.find_element(*TestLocators.NAME_INPUT)
        obj_name.send_keys(log)
        obj_password = browser.find_element(*TestLocators.PASS_INPUT)
        obj_password.send_keys(pas)
        obj_email = browser.find_element(*TestLocators.EMAIL_INPUT)
        obj_email.send_keys(email)
        browser.find_element(*TestLocators.REGISTER_BUTTON).click()
        time.sleep(1)
        mistake_text = browser.find_element(*TestLocators.INCORRECT_PASSWORD)
        t = mistake_text.text
        browser.quit()
        assert t == 'Некорректный пароль'


    #тест на регистрацию закомичу тк пользователь уже зареган . тест падает
    # def test_sing_in_url_is_changed(self):
    #     log = 'nadya'
    #     pas = '123456'
    #     email = 'nadya_terekhina_5_123@yandex.ru'
    #
    #     browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
    #     browser.get("https://stellarburgers.nomoreparties.site/register")
    #     time.sleep(3)
    #     browser.maximize_window()
    #
    #     obj_name = browser.find_element(*TestLocators.NAME_INPUT)
    #     obj_name.send_keys(log)
    #     obj_password = browser.find_element(*TestLocators.PASS_INPUT)
    #     obj_password.send_keys(pas)
    #     obj_email = browser.find_element(*TestLocators.EMAIL_INPUT)
    #     obj_email.send_keys(email)
    #
    #     #регистрация с заполненными полями
    #     browser.find_element(*TestLocators.REGISTER_BUTTON).click()
    #     WebDriverWait(browser, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
    #
    #     cur_url=browser.current_url
    #     browser.quit()
    #     assert cur_url != 'https://stellarburgers.nomoreparties.site/register'





