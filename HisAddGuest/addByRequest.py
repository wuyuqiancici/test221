import requests
import json

class testhis_requests(object):
    def __init__(self):
        pass

    def addNew(self):
        url = 'https://testhis.aiyzy.com/clinic-api/workbench/workbench/register/new'
        headers = {
            'Host': 'testhis.aiyzy.com',
            'Accept': 'application/json,text/plain,*/*',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxODYxMjA1NzcxMSIsInNjb3BlIjpbImFsbCJdLCJpZCI6MjQ0LCJleHAiOjE2Mzg5NDU0MzUsImRlcHRfaWQiOjEyNywiYXV0aG9yaXRpZXMiOlsiNV_otoXnuqfnrqHnkIblkZgiXSwianRpIjoiMjg5YzRhZDAtMDliOC00MjI4LWE1NjctMDkyNGVjZmY1OTIzIiwiY2xpZW50X2lkIjoiY2xpbmljLWFwcCJ9.D2jpQEIIEzkXpd9qcaugGtJqsVd7CdZQEQU - z6QLypN7RamGPRo8eaTWj0JXtDhEr5C3YPHt79pXz0AVRSZ3bPcyp5L4E96E5GzvBk2CkMjhot9OSjQ5G_TdMy4MTgxrjVA6_d4eRDlzsuykjmHIClPH4h6vQiamJWfBlEZEwlw - nglyYB16KKLasEqQdrxHKZYRoAOFUvxaqe2R5PrKFC6cqNNvVqaU6M86ZseFJj69guDfBBTIPfxFNxTWE53HoL0oi66aiQ1DwTvD4wliNpGJXXuGXURLSYz6bfvvWJaICaYq5HuNg_5a2C1Ek0gcCr07gaHfYARtzu9MprpPnw',
            'Origin': 'https://testhis.aiyzy.com',
            'Referer': 'https://testhis.aiyzy.com/',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
            }
        data = {
            "applySurveyCodes": [],
            "birthdate": "2021-11-29",
            "clinicId": 127,
            "gender": 1,
            "idcardNo": "",
            "mobileNo": "18812222233",
            "patientName": "222",
            "serviceRecords": [{"serviceName": "全身检查", "serviceNo": 58}]
             }

        r = requests.post(url=url, data=data, headers=headers)

        print(r.text)


if __name__ == '__main__':
    a = testhis_requests()
    a.addNew()