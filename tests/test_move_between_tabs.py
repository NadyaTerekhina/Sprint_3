from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators_tabs
import time
browser=webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Sprint_3\venv\cromedriver\chromedriver.exe")
browser.get("https://stellarburgers.nomoreparties.site/")
browser.maximize_window()
time.sleep(1)

sauce_tab=WebDriverWait(browser, 7).until(EC.element_to_be_clickable(TestLocators_tabs.SAUCE_TAB))
sauce_tab.click()
time.sleep(1)
sauce_tab_changed=WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_tabs.SAUCE_TAB))
s_dif_class = sauce_tab_changed.get_attribute('class')

def test_click_on_sauces_has_class_current():
    assert 'tab_tab_type_current__2BEPc' in s_dif_class

filling_tab=WebDriverWait(browser, 7).until(EC.element_to_be_clickable(TestLocators_tabs.FILLING_TAB))
filling_tab.click()
time.sleep(1)
filling_tab_changed=WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_tabs.FILLING_TAB))
f_dif_class = filling_tab_changed.get_attribute('class')

def test_click_on_sauces_has_class_current():
   assert 'tab_tab_type_current__2BEPc' in f_dif_class


bread_tab = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(TestLocators_tabs.BREAD_TAB))
bread_tab.click()
time.sleep(1)
bread_tab_changed = WebDriverWait(browser, 7).until(EC.presence_of_element_located(TestLocators_tabs.BREAD_TAB))
b_dif_class = bread_tab_changed.get_attribute('class')

def test_click_on_sauces_has_class_current():
    assert 'tab_tab_type_current__2BEPc' in b_dif_class

browser.quit()
