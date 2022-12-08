from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
browser.get("https://stellarburgers.nomoreparties.site/register")
time.sleep(3)
browser.maximize_window()


log='nadya'
email='nadya_terekhina_5_123@yandex.ru'
pas='123456'

obj_name = browser.find_element(*TestLocators.NAME_INPUT)
obj_name.send_keys(log)
name_value = obj_name.get_property('value')

def test_name_is_not_empty():
    assert len(name_value)!=0

obj_email=browser.find_element(*TestLocators.EMAIL_INPUT)
obj_email.send_keys(email)
email_value = obj_email.get_property('value')

def test_email_in_format_login_god_domain():
    assert "@yandex.ru" in  email_value

obj_password = browser.find_element(*TestLocators.PASS_INPUT)
obj_password.send_keys(pas)
password_value = obj_password.get_property('value')

def test_password_is_6_symbols():
    assert len(password_value)==6

#зарегать пользователя с корректными полями
browser.find_element(*TestLocators.REGISTER_BUTTON).click()

time.sleep(2)

#проверка с некорректным паролем, чистим поле "пароль" и снова нажимаем "зарегистрироваться"

cleared_pass=browser.find_element(*TestLocators.PASS_INPUT)
cleared_pass.send_keys(Keys.CONTROL + "a")
cleared_pass.send_keys(Keys.DELETE)

cleared_pass.send_keys('12345')
browser.find_element(*TestLocators.REGISTER_BUTTON).click()
time.sleep(1)
mistake_text=browser.find_element(*TestLocators.INCORRECT_PASSWORD)
t=mistake_text.text

def test_password_less_than_6_there_is_mistake_in_dom():
    assert t=='Некорректный пароль'

browser.quit()


