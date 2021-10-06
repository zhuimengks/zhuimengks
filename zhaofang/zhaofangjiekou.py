import unittest
import requests



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.url1 = 'http://manager-ehouse-java.itheima.net/api/login/users/signin'
        self.data  = {"username":"admin",
                      "password":"admin"}
        self.headers = {"Content-Type": "application/json"}
        r = requests.put(self.url1,data= self.data,headers =self.headers)
        print (r.text)



if __name__ == '__main__':
    unittest.main()
