import yaml

f = open('./../testhis.yml', encoding='utf-8')
data = yaml.load(f, Loader=yaml.FullLoader)

ip = data["testhis域名"]

# 登录页
login = data["登录页确定键"]
# 新增待检用户信息完善页
name = data["姓名输入框"]
sex = data["性别单选框"]
man = data["性别男"]
woman = data["性别女"]
birth = data["出生日期输入框"]
birthday = data["出生日期"]
doctorselect = data["医生选择框"]
doctor = data["选择医生"]
dateselect = data["预约日期选择框"]
date = data["预约日期"]
timeselect = data["预约时间选择框"]
time = data["预约时间"]
manexamine = data["男性全检"]
womanexamine = data["女性全检"]
bodyexamine = data["全身检查"]
faceexamine = data["面部检查"]
submit = data["提交按钮"]
# 预约签到页
arrive = data["已到诊按钮"]
arriveconfirm = data["确定到诊"]
# 预约收费页
othercharge = data["其他收费按钮"]
chargeconfirm = data["确定收费"]
datesearch = data["日期搜索框"]
datetosearch = data["选择搜索日期"]
search = data["搜索按钮"]

# 活动登记页
add = data["registerPage"]["新增按钮"]
telinput = data["registerPage"]["手机号输入框"]
nameinput = data["registerPage"]["姓名输入框"]
sexinput = data["registerPage"]["性别单选框"]
male = data["registerPage"]["性别男"]
female = data["registerPage"]["性别女"]
birthinput = data["registerPage"]["出生日期输入框"]
birthdayreg = data["registerPage"]["出生日期"]
allexamine = data["registerPage"]["全身检查"]
registconfirm = data["registerPage"]["确定登记按钮"]