from properties import *
from constants import *
from library import *
from time import sleep

control_obj = Common()
class TestFlipkart:
    def test1(self):
        control_obj.goto_url(URL)

        control_obj.settext(email_xpath,EMAIL_ID,name='mail_textbox')
        control_obj.settext(password_xpath,PASSWORD,name="password_textbox")
        control_obj.click(login_submit_xpath, name='login_submit')
        control_obj.waitfortheelement_to_load(search_textbox_xpath,elementname="search_textbox")
        control_obj.settext(search_textbox_xpath,"samsung",name="search_textbox")


if __name__ == '__main__':
    t = TestFlipkart()
    t.test1()
