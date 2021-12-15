import unittest
import requests



class MyTestCase(unittest.TestCase):
    def test_login(self):
        self.url1 = 'http://portal-ehouse-java.itheima.net/api/login/users/signin'
        self.params = {"username":"chenchuan",
                       "password":"123456"}
        self.headers = {"Content-Type": "application/json"}
        #r = requests.put(self.url1,data= self.data,headers =self.headers)
        r = requests.put(self.url1, json = self.params)
        print (r.text)
        #接口为put接口所以参数放置不一样
        print (r.json()['token']) #获得返回接口中的token

        #房屋列表接口
        self.url2 = 'http://portal-ehouse-java.itheima.net/api/house-order/sales/list'
        self.headers2 = {"Content-Type": "application/json",
                        "Authorization":r.json()['token']}
        r2 = requests.get(self.url2,headers =self.headers2 )
        print(r2.text)
        #立即选购接口
        self.url3 = 'http://portal-ehouse-java.itheima.net/api/house-order/sales/details/32038'
        r3 = requests.get(self.url3,headers =self.headers2 )
        print(r3.text)
        print(r3.json()[0]['houseOrders'][5]['id']) #获取房屋的ID编号
        print(r3.json()[0]['houseOrders'][5]['houseId'])#获取房屋的houseId编号
        #房屋购买接口
        print("房屋购买")
        self.url4 = 'http://portal-ehouse-java.itheima.net/api/house-order/house_orders/32038/1197/35061'
        #self.params4 = {"houseId": r3.json()[0]['houseOrders'][5]['houseId'],
                        #"id": r3.json()[0]['houseOrders'][5]['id']}
        r4 = requests.put(self.url4, headers =self.headers2)
        print(r4.text)
        #收藏接口,房屋编号可以变换
        print("收藏接口")
        self.url5 = 'http://portal-ehouse-java.itheima.net/api/house-order/house_orders/35061/add_favorite'
        r5 = requests.put(self.url5,headers =self.headers2)
        print(r5.text)
        #我的收藏列表
        print("我的收藏接口")
        self.url7= 'http://portal-ehouse-java.itheima.net/api/user-center/favorites'
        r7 = requests.get(self.url7,headers =self.headers2)
        print(r7.text)
        #我的订单
        print("我的订单接口")
        self.url6 = 'http://portal-ehouse-java.itheima.net/api/user-center/buyHouseOrderState'
        r6 = requests.get(self.url6, headers=self.headers2)
        print(r6.text)

        print("取消购买")
        self.url8 = 'http://portal-ehouse-java.itheima.net/api/house-order/house_orders/1197/cancel/35061'
        r8 =requests.put(self.url8,headers=self.headers2)
        print(r8)












if __name__ == '__main__':
    unittest.main()

