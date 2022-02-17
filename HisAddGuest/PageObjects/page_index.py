"""
页面类：
封装在当前页面或者这个流程上的基本方法
便于后续的复用以及维护
类似的方法在不同页面上可能对应不同的操作，故针对页面进行封装更清晰，解耦
比如点击方法，在有的页面上是双击，有的页面上是点击并悬停，等待
"""

from HisAddGuest.Base.BasePage import BasePage
from HisAddGuest import testhis_yaml


class loginPageIndex(BasePage):
    def open_testhis(self):
        self.get_url('https://%s' % testhis_yaml.ip)

    def username_send(self, selector, username):
        self.text_send(selector, username)

    def password_send(self, selector, password):
        self.text_send(selector, password)

    def click(self, selector):
        self.click_option(selector)


class appointmentPageIndex(BasePage):
    def open_appointpage(self):
        self.get_url('https://%s/#/workbench/appointment/list' % testhis_yaml.ip)

    def click(self, selector):
        self.click_option(selector)

    def send_keys(self, selector, keys):
        self.text_send(selector, keys)

    def slide_to_bottom(self):
        js = "var q=document.documentElement.scrollTop=100000"  # 滑动页面到底部
        self.driver.execute_script(js)


class chargePageIndex(BasePage):
    def open_chargepage(self):
        self.get_url('https://%s/#/workbench/appointmentfee/list' % testhis_yaml.ip)

    def click(self, selector):
        self.click_option(selector)


class registerPageIndex(BasePage):
    def open_registerpage(self):
        self.get_url('https://%s/#/survey/registration-check/list' % testhis_yaml.ip)

    def click(self, selector):
        self.click_option(selector)

    def send_keys(self, selector, keys):
        self.text_send(selector, keys)
