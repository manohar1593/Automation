from properties import *
from constants import *
from library import *

control_obj = Common()
class TestFlipkart:
    def test1(self):
        control_obj.goto_url(URL)
        control_obj.win_maximize()
        # control_obj.waitfortheelement_to_load(login_main_button,elementname="login main btn")
        # control_obj.click(login_main_button,name="main login btn")
        control_obj.waitfortheelement_to_load(email_xpath, logmsg="mail_textbox")
        control_obj.settext(email_xpath,EMAIL_ID,logmsg='mail_textbox')
        control_obj.settext(password_xpath,PASSWORD,logmsg="password_textbox")
        control_obj.click(login_submit_xpath, logmsg='login_submit')
        time.sleep(1)
        control_obj.waitfortheelement_to_load(search_textbox_xpath,logmsg="search_textbox")
        control_obj.settext(search_textbox_xpath,"televi",logmsg="search_textbox")
        control_obj.select_any_product_from_searchlist(search_dynamic_pop_up,logmsg="product_popup")
        control_obj.goto_page_number(page_num_xpath,logmsg="page_no")
        control_obj.select_product(product,2,logmsg="2nd_product")
        control_obj.switch_to_window(1)
        control_obj.scroll_to_middle()
        control_obj.scroll_down()
        control_obj.scroll_up()
        control_obj.waitfortheelement_to_load(buy_now,logmsg="buy_now")
        control_obj.click(buy_now,logmsg="buy_now")
        control_obj.waitfortheelement_to_load(continue_xpath,logmsg="Continue_button")
        control_obj.take_screenshot()
        time.sleep(2)
        control_obj.driver.quit()

if __name__ == '__main__':
    t = TestFlipkart()
    t.test1()
