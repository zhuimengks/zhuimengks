import unittest
import requests
import json


class Zhuhuixuecheng(unittest.TestCase):
    def test_login(self):
        self.url = 'http://main-xc-java.itheima.net/xuecheng/common/login'
        self.header = {'Content-Type': 'application/json'}
        params ={"username":"admin","password":"admin","verifycode":"1234"}
        r = requests.post(self.url,headers = self.header,data = json.dumps(params))

        print (r.json())




if __name__ == '__main__':
    unittest.main()
