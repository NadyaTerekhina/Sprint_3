from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators_login
from locators import TestLocators_buttons_login
import time



browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
browser.get("https://stellarburgers.nomoreparties.site/")
time.sleep(3)
browser.maximize_window()


def f_log_in(email, pas):
   email_field = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
   email_field.send_keys(email)
   pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys(pas)
   log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()

#переходит во "вход" по кнопке "войти в аккаунт"
WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_LOGIN_BUTTON)).click()
time.sleep(1)
f_log_in(email='nadya_terekhina_5_123@yandex.ru', pas='123456')
time.sleep(1)
cur_url_1=browser.current_url
#вход через кнопку " войти в аккаунт"
def test_log_in_in_login_site():
   assert "login" not in cur_url_1





browser.quit()