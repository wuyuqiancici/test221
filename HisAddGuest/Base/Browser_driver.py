"""
封装浏览器引擎处理
"""

import os
from selenium import webdriver


class BrowserDriver(object):
    def open_borwser(self, browser):
        """设定浏览器类型"""
        global driver
        if "Chrome" == browser:
            chrome_driver_path = os.path.dirname(os.path.abspath(".")) + "/Utils/chromedriver.exe"
            driver = webdriver.Chrome(executable_path=chrome_driver_path)
            #driver = webdriver.Chrome()

        elif "firefox" == browser:
            fire_driver_path = os.path.dirname(os.path.abspath(".")) + "/Utils/firefoxdriver.exe"
            driver = webdriver.Firefox(executable_path=fire_driver_path)

        driver.maximize_window()
        driver.implicitly_wait(15)
        return driver

"""
将驱动放到python.exe同一目录下，则不需要指定驱动路径
"""