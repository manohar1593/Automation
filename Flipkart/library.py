'''
ui common methods implemented here
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import *
import time,random

class Common:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def goto_url(self,url):
        self.driver.get(url)

    def verify_element_is_visible(self,locator,timeout):
        pass
    def waitfortheelement_to_load(self,locator,timeout=30,elementname=''):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            error_message = "Unable to load - " + elementname

            raise Exception(error_message)
    def get_element_handle(self,locator,timeout=30,elementname=''):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            return ele
        except TimeoutException:
            error_message = "Unable to get element " + elementname
            raise Exception(error_message)

    def click(self,locator,timeout=30,name=''):
        ele = self.get_element_handle(locator)
        ele.click()

    def settext(self,locator,textbox_value,name=''):
        ele = self.get_element_handle(locator,elementname=name)
        try:
            ele.click()
            ele.clear()
            ele.send_keys(textbox_value)
        except:
            error_message = "Unable to enter value-"+textbox_value
            raise Exception(error_message)

    def get_search_list(self,locator,name=''):
        self.waitfortheelement_to_load(locator)
        ele_list = self.driver.find_elements_by_xpath(locator)
        return ele_list

    def select_any_product_from_list(self,locator,name=''):
        ele_list = self.get_search_list(locator,name)
        product = random.choice(ele_list)
        product.click()








