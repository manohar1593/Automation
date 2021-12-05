'''
ui common methods implemented here
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import *
from properties import last_element,first_element,backtotop,rating
import time,random

class Common:

    def __init__(self):
        '''
        Constructor and Launching the browser
        '''
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def goto_url(self,url):
        '''
        Open the flipkart link
        '''
        self.driver.get(url)

    def win_maximize(self):
        '''
        Maximizing the Window
        '''
        self.driver.maximize_window()


    def waitfortheelement_to_load(self,locator,timeout=30,logmsg=''):
        '''
        Waiting for the Element to be Loaded
        '''
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            while(timeout): #stale element exception handled
                try:
                    if ele.is_displayed() and ele.is_enabled():
                        break
                except:
                    print("Exception occured")
                ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
                timeout = timeout - 1
                time.sleep(1)
        except TimeoutException:
            error_message = "Unable to load - " + logmsg

            raise Exception(error_message)


    def get_element_handle(self,locator,timeout=30,logmsg=''):
        '''
        Getting the element handle
        '''
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
            return ele
        except TimeoutException:
            error_message = "Unable to get element " + logmsg
            raise Exception(error_message)


    def click(self,locator,timeout=30,logmsg=''):
        '''
        To click the element
        '''
        time.sleep(2)
        ele = self.get_element_handle(locator)
        if ele.is_displayed() and ele.is_enabled():
            ele.click()
        else:
            print("element- is not displayed/enabled".format(logmsg))


    def settext(self,locator,textbox_value,logmsg=''):
        '''
        Sending Values
        '''
        timeout = 5
        while timeout:  #This code to handle stale element exception

            try:
                ele = self.get_element_handle(locator, logmsg=logmsg)
                ele.click()
                break
            except WebDriverException:
                print("Got timeout Exception")
                timeout = timeout - 1
                time.sleep(0.5)

        # Enter Text value code
        ele = self.get_element_handle(locator,logmsg=logmsg)
        try:
            ele.click()
            ele.clear()
            ele.send_keys(textbox_value)
        except:
            error_message = "Unable to enter value-"+textbox_value
            raise Exception(error_message)


    def get_search_list(self,locator,logmsg=''):
        '''
        To get the list of items in the search textbox popup
        '''
        self.waitfortheelement_to_load(locator,logmsg=logmsg)
        ele_list = self.driver.find_elements_by_xpath(locator)
        return ele_list


    def select_any_product_from_searchlist(self,locator,logmsg=''):
        '''
        This library call selects product contains televisions text  from search text box popup
        '''
        ele_list = self.get_search_list(locator,logmsg)
        for product in ele_list:
            if "televisions" in product.text:
                time.sleep(0.5)
                product.click()
                break
        timer=3
        while(timer): # to handle click issue
            try:
                ele_list = self.get_search_list(locator, logmsg)
                if ele_list:
                    for product in ele_list:
                        if "televisions" in product.text:
                            time.sleep(0.5)
                            product.click()
                            break
                    timer = timer - 1
                    time.sleep(1)
                else:
                    break
            except:
                break



    def goto_page_number(self,locator,page_no=3,logmsg=''):
        '''
        Selecting the page no (by default 3)
        '''
        loc = locator.format(page_no)
        self.waitfortheelement_to_load(loc,logmsg=logmsg)
        self.click(loc,logmsg=logmsg)


    def switch_to_window(self,tab_index):
        '''
        Switching window to product window
        '''
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[int(tab_index)])
        else:
            print("unable to switch window")
            exit(-1)


    def select_product(self,locator,product:int,logmsg=''):
        '''
        Selecting product
        :product - product number
        '''
        product_num = locator.format(product)
        self.waitfortheelement_to_load(product_num, logmsg=logmsg)
        self.click(product_num, logmsg=logmsg)
        timer=5
        while (timer):
            if len(self.driver.window_handles)>1:
                break
            self.click(product_num, logmsg=logmsg)
            timer=timer-1
            time.sleep(1)

    def scroll_down(self):
        '''
        Scrolling down
        '''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_middle(self):
        '''
        Scrolling to middle of the page
        '''
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2);")


    def take_screenshot(self):
        '''
        Taking Screenshot and saving in the path specified.
        '''
        self.driver.save_screenshot(PATH)


    def scroll_up(self):
        '''
        Scrolling Up
        '''
        timer=60
        self.waitfortheelement_to_load(backtotop)
        while(timer):
            try:
                ele= self.driver.find_element_by_xpath(backtotop)
                if not (ele.is_displayed() and ele.is_enabled()):
                    break
                self.driver.execute_script("scrollBy(0,-1000);")
                time.sleep(1)
                timer = timer - 1
            except:
                break








