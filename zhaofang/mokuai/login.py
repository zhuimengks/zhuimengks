import requests
import json
import unittest
import requests, json
import re
#登录

#class Zhiwei(unittest.TestCase):

def test_denglu(self):
    url1 = "http://portal-ehouse-java.itheima.net/api/login/users/signin"
    data = {
        "username": "chenchuan",
        "password": "123456"
    }
    headers = {"Content-Type": "application/json"}
    res = requests.put(url=url1, data=json.dumps(data), headers=headers)
    res_1 = res.json()    #返回的类型还未转换为json格式

    print("登录token是:"+res_1["token"])


    return res_1["token"]
#if __name__ == '__main__':
#    unittest.main()





