"""
将所有基础操作，比如：打开URL，关闭浏览器，点击，输入，获取元素
一切不可能发生变化的逻辑进行封装
"""


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 打开URL
    def get_url(self, url):
        self.driver.get(url)

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 获取元素 arr = []
    def findElement(self, selector):
        ele = self.driver.find_element(*selector)
        return ele

    # 输入字符
    def text_send(self, selector, text):
        ele = self.findElement(selector)
        ele.clear()
        ele.send_keys(text)

    # 清空
    def clear(self, selector):
        ele = self.findElement(selector)
        ele.clear()

    # 点击
    def click_option(self, selector):
        ele = self.findElement(selector)
        ele.click()

    # 获取页面title
    def get_page_title(self):
        return self.driver.title

    # 获取页面url断言
    def get_page_url(self):
        return self.driver.current_url

    # 切换到新的窗口
    def switch_handle(self, num):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[num])
