import requests
import json
import unittest
import login




class Zhiwei_list(unittest.TestCase):
    def test_list(self):
        s = login.Zhiwei.test_denglu(self)
        url2 = "http://portal-ehouse-java.itheima.net/api/house-order/sales/list"
        headers2 = {"Content-Type": "application/json",
                   "Authorization":s}
        re2 = requests.get(url=url2,headers = headers2)
        print(re2.text)



if __name__ == '__main__':
    unittest.main()


