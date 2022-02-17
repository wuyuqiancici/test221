import schedule
from HisAddGuest.TestSuits.addGuest_li import testAddGuest02
from HisAddGuest.TestSuits.addGuest_li import testAddGuest01
import time

def func1():
    accounts = [18612057710, 18612057711, 18612057712, 18612057713, 18612057714]
    orgname_list = ['测试机构1', '测试机构2', '测试机构3', '测试机构4', '测试机构5']
    for i in range(len(accounts)):
        testAddGuest02(accounts[i], 10, orgname_list[i])

def func2():
    testAddGuest01(15011440328, 10, '_')

# schedule.every().day.at("00:01").do(func1)
schedule.every().day.at("00:10").do(func2)

while True:
    # run_pending：运行所有可以运行的任务
    schedule.run_pending()
    time.sleep(1)