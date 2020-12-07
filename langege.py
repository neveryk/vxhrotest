import json
import datetime
from time import sleep
import requests
import random
def token():
    herder={
        "Host":"vxapipad.knx.com.cn",
        "Accept":"*/*",
        "version":"9.0.0",
        "X-Requested-With":"XMLHttpRequest",
        "expertphone":"",
        "Accept-Language":"zh-cn",
        "Accept-Encoding":"gzip, deflate",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Origin":"ionic://localhost",
        "Content-Length":"298",
        "language":"zh-cn",
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C104",
        "Connection":"keep-alive"
    }
    data={
    "account":"19186951486",
    "password":"MjczMDE1",
    "comid":"moumou",
    "uuid":"C25913789F75BA62B83149082CD7E79C",
    "userId":"0",
    "empId":""
    }
    url='http://vxapipad.knx.com.cn/UserLogin/UserLogin'
    r=requests.post(url,headers=herder,data=data)
    g=json.loads(r.text)
    auth=g['data']['auth']
    return auth

def click_morning_daka(token):
    header={
        "Host":"vxapipad.knx.com.cn",
        "version":"9.0.0",
        "X-Requested-With":"XMLHttpRequest",
        "auth":token,
        "Accept-Language":"zh-cn",
        "Accept-Encoding":"gzip,deflate",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Origin":"ionic://localhost",
        "Content-Length":"301",
        "language":"zh-cn",
        "User-Agent":"Mozilla/5.0(iPhone;CPU iPhoneOS12_1_2likeMacOSX)AppleWebKit / 605.1.15(KHTML,likeGecko)Mobile / 16C104",
        "Connection":"keep-alive"
    }
    data={
        "address":"湖南省长沙市天心区芙蓉南路辅路",
        "longitude":"112.989327694383",
        "latitude":"28.0748353763493",
        "uuid":"B4064697-87AA-4FCA-9098-8426E766FCAF",
        "deviceName":"iPhone11, 8",
        "sourcetype":"0",
        "maptype":"2",
        "userId":"0",
        "empId":"13"
    }
    r_time=random.randint(60,180)

    morning_time_action = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '08:40', '%Y-%m-%d%H:%M')
    mornint_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '08:55', '%Y-%m-%d%H:%M')

    # 当前时间
    n_time = datetime.datetime.now()

    if n_time > morning_time_action and n_time < mornint_time_end:
        sleep(r_time)
        url1='http://vxapipad.knx.com.cn/SaveMobileAttendanceRecord'
        re=requests.post(url1,headers=header,data=data)
        response=re.text.encode('utf-8')
        text=json.loads(response)
        message=text["errorMsg"]
        print("早上"+message+"打卡时间"+str(n_time))
        return message
    else:
        sleep(5)
        print('早上还未到打卡时间')
def click_night_daka(token):
    header = {
        "Host": "vxapipad.knx.com.cn",
        "version": "9.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "auth": token,
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip,deflate",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "ionic://localhost",
        "Content-Length": "301",
        "language": "zh-cn",
        "User-Agent": "Mozilla/5.0(iPhone;CPU iPhoneOS12_1_2likeMacOSX)AppleWebKit / 605.1.15(KHTML,likeGecko)Mobile / 16C104",
        "Connection": "keep-alive"
    }
    data = {
        "address": "湖南省长沙市天心区芙蓉南路辅路",
        "longitude": "112.989327694383",
        "latitude": "28.0748353763493",
        "uuid": "B4064697-87AA-4FCA-9098-8426E766FCAF",
        "deviceName": "iPhone11, 8",
        "sourcetype": "0",
        "maptype": "2",
        "userId": "0",
        "empId": "13"
    }
    r_time = random.randint(60, 180)

    night_time_actione = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '17:40', '%Y-%m-%d%H:%M')
    night_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '18:00', '%Y-%m-%d%H:%M')

    # 当前时间
    n_time = datetime.datetime.now()

    if n_time > night_time_actione and n_time < night_time_end:
        sleep(r_time)
        url1 = 'http://vxapipad.knx.com.cn/SaveMobileAttendanceRecord'
        re = requests.post(url1, headers=header, data=data)
        response = re.text.encode('utf-8')
        text = json.loads(response)
        message = text["errorMsg"]
        print("晚上" + message+"打卡时间"+str(n_time))
        return message
    else:
        sleep(5)
        print('晚上还未到打卡时间')
if __name__ == '__main__':
    # 晚上
    while True:
        to = token()
        text = click_night_daka(to)
        if text == '打卡成功':
            break
        else:
            print('打卡失败')
            print('-------')
    # 早上
    while True:
        to=token()
        text=click_morning_daka(to)
        if text=='打卡成功':
            break
        else:
            print('打卡失败')
            print('-------')


