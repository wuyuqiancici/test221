from HisAddGuest.Flow.TestFlow import loginFlow, appointFlow, chargeFlow, registerFlow
from HisAddGuest.Base.Browser_driver import BrowserDriver


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


if __name__ == '__main__':
    # 需要执行添加待检用户的机构账号
    # accounts = [18612057710, 18612057711, 18612057712, 18612057713, 18612057714]
    # orgname_list = ['测试机构1', '测试机构2', '测试机构3', '测试机构4', '测试机构5']
    # for i in range(len(accounts)):
    #     testAddGuest02(accounts[i], 10, orgname_list[i])

    testAddGuest02(18612057710, 10, '测试机构1')


    # 正式环境测试机构16添加用户
    # testAddGuest01(15011440328, 20, '_')