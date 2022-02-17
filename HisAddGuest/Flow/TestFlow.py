"""
流程类 -- 将测试步骤打包到一起
流程:
 肆意组合页面中的内容 操作
"""

from HisAddGuest.PageObjects import page_index
from selenium.webdriver.common.by import By
import time
from HisAddGuest import testhis_yaml


class loginFlow(page_index.loginPageIndex):
    def login(self, username, password):
        self.open_testhis()
        self.username_send((By.NAME, 'username'), username=username)
        self.password_send((By.NAME, 'password'), password=password)
        self.click((By.XPATH, testhis_yaml.login))
        #self.click((By.XPATH, '//*[@id="app"]/div/form/button'))
        time.sleep(5)
        result = self.get_page_title()  # 首页 - 诊所端系统
        return result


class appointFlow(page_index.appointmentPageIndex):
    def enter_registpage(self, tel):
        self.open_appointpage()
        #  输入手机号进入登记信息页面
        # self.click((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span'))  # 点击预约签到
        # time.sleep(1)
        # self.click((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/header/button/span'))  # 点击预约
        # time.sleep(1)
        # self.send_keys((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/input'), tel)  # 输入手机号
        # self.click((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div[2]/div/div/div[3]/span/button[2]/span'))  # 点击确定
        time.sleep(1)
        # 或直接通过URL进入登记信息页面
        self.get_url('https://%s/#/workbench/appointment/add?phone=%d' % (testhis_yaml.ip,tel))
        time.sleep(2)
        result = self.get_page_title()  # 新增预约签到 - 诊所端系统
        return result

    def complete_info(self, name, sex):
        #  填写登记信息
        #  输入姓名
        self.send_keys((By.XPATH, testhis_yaml.name), name)
        #  选择性别
        self.click((By.XPATH, testhis_yaml.sex))
        time.sleep(1)
        if sex == 1:
            self.click((By.XPATH, testhis_yaml.man))  #  选择男
        elif sex == 0:
            self.click((By.XPATH, testhis_yaml.woman))  #  选择女
        #  选择出生日期,目前每次使用前需手动更改tr和td的索引值，tr行，td列
        self.click((By.XPATH, testhis_yaml.birth))
        self.click((By.XPATH, testhis_yaml.birthday))
        #  滑动页面到底部
        self.slide_to_bottom()
        #  点击预约专家
        self.click((By.XPATH, testhis_yaml.doctorselect))
        time.sleep(1)
        #  选择第一个医生
        self.click((By.XPATH, testhis_yaml.doctor))
        #  点击预约日期
        self.click((By.XPATH, testhis_yaml.dateselect))
        time.sleep(1)
        #  待优化，选择日期，目前每次使用前需手动更改tr和td的索引值，tr行，td列
        self.click((By.XPATH, testhis_yaml.date))

        #  滑动页面到底部
        self.slide_to_bottom()
        time.sleep(1)
        #  点击预约时间
        self.click((By.XPATH, testhis_yaml.timeselect))
        time.sleep(1)
        #  选择第2个时间段
        self.click((By.XPATH, testhis_yaml.time))
        # 选择全身检查
        self.click((By.XPATH, testhis_yaml.bodyexamine))
        time.sleep(1)
        self.click((By.XPATH, testhis_yaml.faceexamine))
        time.sleep(1)
        # if (sex == 1):
        #     #  选择男性全检
        #     self.click((By.XPATH, testhis_yaml.manexamine))
        # elif (sex == 0):
        #     #  选择女性全检
        #     self.click((By.XPATH, testhis_yaml.womanexamine))
        #  点击提交
        self.click((By.XPATH, testhis_yaml.submit))
        time.sleep(5)


    def arrive(self):
        self.open_appointpage()
        time.sleep(1)
        #  点击已到诊按钮
        self.click((By.XPATH, testhis_yaml.arrive))
        time.sleep(1)
        #  点击确定
        self.click((By.XPATH, testhis_yaml.arriveconfirm))
        time.sleep(3)


class chargeFlow(page_index.chargePageIndex):
    def charge(self):
        self.open_chargepage()
        time.sleep(2)
        # #  点击日期搜索框
        # self.click((By.XPATH, testhis_yaml.datesearch))
        # time.sleep(1)
        # #  选择搜索日期
        # self.click((By.XPATH, testhis_yaml.datetosearch))
        # self.click((By.XPATH, testhis_yaml.datetosearch))
        # #  点击搜索
        # self.click((By.XPATH, testhis_yaml.search))
        # time.sleep(1)
        #  点击其他收费
        self.click((By.XPATH, testhis_yaml.othercharge))
        time.sleep(1)
        #  点击确定
        self.click((By.XPATH, testhis_yaml.chargeconfirm))
        time.sleep(5)


class registerFlow(page_index.registerPageIndex):
    def register(self, tel, name, sex):
        self.open_registerpage()
        time.sleep(2)
        # 点击新增
        self.click((By.XPATH, testhis_yaml.add))
        time.sleep(1)
        # 输入手机号
        self.send_keys((By.XPATH, testhis_yaml.telinput), tel)
        #  输入姓名
        self.send_keys((By.XPATH, testhis_yaml.nameinput), name)
        #  选择性别
        self.click((By.XPATH, testhis_yaml.sexinput))
        time.sleep(1)
        if sex == 1:
            self.click((By.XPATH, testhis_yaml.male))  #  选择男
        elif sex == 0:
            self.click((By.XPATH, testhis_yaml.female))  #  选择女
        #  选择出生日期,目前每次使用前需手动更改tr和td的索引值，tr行，td列
        self.click((By.XPATH, testhis_yaml.birthinput))
        time.sleep(1)
        self.click((By.XPATH, testhis_yaml.birthdayreg))
        # 勾选全身检查,修改label后的索引值可以勾选不同的项目
        self.click((By.XPATH, testhis_yaml.allexamine))
        # 点击确定
        self.click((By.XPATH, testhis_yaml.registconfirm))
        time.sleep(3)