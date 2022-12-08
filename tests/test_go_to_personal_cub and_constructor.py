from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators_login
from locators import TestLocators_buttons_login
import time

def f_log_in(email, pas):
   email_field = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
   email_field.send_keys(email)
   pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys(pas)
   log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()

browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
browser.get('https://stellarburgers.nomoreparties.site/login')
browser.maximize_window()
time.sleep(1)
f_log_in(email='nadya_terekhina_5_123@yandex.ru', pas='123456')

button_personal=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()

time.sleep(1)

cur_url_pers=browser.current_url
def test_go_to_personal_cub_with_personal_but():
   assert "/account/profile"  in cur_url_pers

button_constructor=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_CONSTRUCTOT_BUTTON)).click()
time.sleep(1)
home_page=browser.current_url
print(home_page)

def test_go_to_constructor_with_constructor_but():
   assert home_page == 'https://stellarburgers.nomoreparties.site/'

#возвращаемся в личный кабинет
button_personal=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()

time.sleep(1)


stellar_logo_button=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_STELLAR_LOGO_BUTTON)).click()
time.sleep(1)
cur_start_page=browser.current_url
def test_go_to_constructor_with_logo_but():
   assert cur_start_page == 'https://stellarburgers.nomoreparties.site/'

#возвращаемся в личный кабинет
button_constructor=WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
time.sleep(1)

log_out_but =WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.PERSONAL_CUB_LOG_OUT_BUTTON)).click()
time.sleep(1)
log_out_url = browser.current_url
def test_log_out_in_pers_cub():
   assert log_out_url == 'https://stellarburgers.nomoreparties.site/login'

browser.quit()
