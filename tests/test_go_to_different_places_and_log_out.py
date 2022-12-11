from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators_login
from locators import TestLocators_buttons_login
import time



class TestGoTo:
   def test_go_to_personal_cub_with_personal_button(self):
      browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
      browser.get('https://stellarburgers.nomoreparties.site/login')
      browser.set_window_size(1920, 1080)
      # логин в систему
      email_field = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
      email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
      pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys('123456')
      log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
      WebDriverWait(browser, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
   ####
      button_personal=WebDriverWait(browser, 10).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
      WebDriverWait(browser, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
      cur_url_pers=browser.current_url
      browser.quit()
      assert "/account/profile"  in cur_url_pers

   def test_go_to_constructor_with_constructor_button(self):
      browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
      browser.get('https://stellarburgers.nomoreparties.site/login')
      browser.set_window_size(1920, 1080)
      #логин в систему
      email_field = WebDriverWait(browser, 7).until( EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
      email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
      pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys('123456')
      log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
      #переход в личный кабинет
      button_personal = WebDriverWait(browser, 10).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
      WebDriverWait(browser, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
       #переход в конструкто по кнопке "конструктор"
      button_constructor = WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_CONSTRUCTOT_BUTTON)).click()
      home_page = browser.current_url
      browser.quit()
      assert home_page == 'https://stellarburgers.nomoreparties.site/'

   def test_go_to_constructor_with_logo_button(self):
      browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
      browser.get('https://stellarburgers.nomoreparties.site/login')
      browser.set_window_size(1920, 1080)
      # логин в систему
      email_field = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
      email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
      pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys('123456')
      log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
      # переход в личный кабинет
      button_personal = WebDriverWait(browser, 10).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
      WebDriverWait(browser, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
      #переход в конструктор по лого
      stellar_logo_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_STELLAR_LOGO_BUTTON)).click()
      cur_start_page = browser.current_url
      assert cur_start_page == 'https://stellarburgers.nomoreparties.site/'

   def test_out_in_pers_cub(self):
      browser = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
      browser.get('https://stellarburgers.nomoreparties.site/login')
      browser.set_window_size(1920, 1080)
      # логин в систему
      email_field = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_login.EMAIL_INPUT_LOGIN))
      email_field.send_keys('nadya_terekhina_5_123@yandex.ru')
      pas_field = browser.find_element(*TestLocators_login.PASS_INPUT_LOGIN).send_keys('123456')
      log_in_button = browser.find_element(*TestLocators_login.lOG_IN_BUTTON).click()
      # переход в личный кабинет
      button_personal = WebDriverWait(browser, 10).until(EC.presence_of_element_located(TestLocators_buttons_login.HOME_PAGE_PERSONAL_BUTTON)).click()
      WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
      ####
      log_out_but = WebDriverWait(browser, 5).until(EC.presence_of_element_located(TestLocators_buttons_login.PERSONAL_CUB_LOG_OUT_BUTTON)).click()
      WebDriverWait(browser, 10).until_not(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
      log_out_url = browser.current_url
      browser.quit()
      assert log_out_url == 'https://stellarburgers.nomoreparties.site/login'
