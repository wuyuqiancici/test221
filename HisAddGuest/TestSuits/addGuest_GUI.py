from HisAddGuest.Flow.TestFlow import loginFlow, appointFlow, chargeFlow, registerFlow
from HisAddGuest.Base.Browser_driver import BrowserDriver
from tkinter import *
import threading

def testAddGuest01(account, personCount, orgName):
    # 通过护士站流程进行客户添加
    driver = BrowserDriver().open_borwser('Chrome')
    loginTest = loginFlow(driver)
    appointTest = appointFlow(driver)
    chargeTest = chargeFlow(driver)

    loginTest.login(account, '123456')

    tellist = []
    tel = None
    if account == 18612057710:
        tel = 18601111111
    elif account == 18612057711:
        tel = 18611111111
    elif account == 18612057712:
        tel = 18621111111
    elif account == 18612057713:
        tel = 18631111111
    elif account == 18612057714:
        tel = 18641111111
    elif account == 15011440328:
        tel = 18651111111
    namelist = []
    nameNum = 1
    sexlist = []
    for i in range(personCount):
        tellist.append(tel)
        tel = tel + 1
        namelist.append(orgName + "待检人" + str(nameNum))
        nameNum = nameNum + 1
        if i % 2 == 0:
            sexlist.append(1)
        else:
            sexlist.append(0)

    for i in range(personCount):
        appointTest.enter_registpage(tellist[i])
        appointTest.complete_info(namelist[i], sexlist[i])
        chargeTest.charge()
        appointTest.arrive()

    driver.quit()


def testAddGuest02(account, personCount, orgName):
    # 通过预约登记进行客户添加，account---机构对应的登录账号，personCount--预计添加的人数
    driver = BrowserDriver().open_borwser('Chrome')
    # 实例化对象
    loginTest = loginFlow(driver)
    registerTest = registerFlow(driver)
    # 执行登录
    loginTest.login(account, '123456')
    # 根据人数配置人员信息，电话、姓名、性别
    tellist = []
    tel = None
    if account == 18612057710:
        tel = 18601111111
    elif account == 18612057711:
        tel = 18611111111
    elif account == 18612057712:
        tel = 18621111111
    elif account == 18612057713:
        tel = 18631111111
    elif account == 18612057714:
        tel = 18641111111
    elif account == 19801331985:
        tel = 18651111111

    namelist = []
    nameNum = 1
    sexlist = []
    for i in range(personCount):
        tellist.append(tel)
        tel = tel + 1
        namelist.append(orgName + "待检人" + str(nameNum))
        nameNum = nameNum + 1
        if i % 2 == 0:
            sexlist.append(1)
        else:
            sexlist.append(0)
    # 执行预约登记操作
    for i in range(personCount):
        registerTest.register(tellist[i], namelist[i], sexlist[i])

    driver.quit()

def run(account, personCount, orgName):
    t = threading.Thread(target=testAddGuest02,args=(account, personCount, orgName))
    t.start()

if __name__ == '__main__':
    root = Tk()
    root.title('自动化添加testhis系统的待检用户')
    root.geometry('720x480')

    account_lb = Label(root, text='登录账号')
    account_lb.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.05)
    account = Entry(root)
    account.place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.05)

    orgname_lb = Label(root, text='机构名称')
    orgname_lb.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.05)
    orgname = Entry(root)
    orgname.place(relx=0.4, rely=0.3, relwidth=0.3, relheight=0.05)

    num_lb = Label(root, text='添加人数')
    num_lb.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.05)
    num = Entry(root)
    num.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.05)

    btn_run = Button(root, text="start",command=lambda : run(int(account.get()),int(num.get()),orgname.get()))  # 注意传参需要使用匿名函数lambda
    btn_run.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.1)

    root.mainloop()