
import unittest

from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner

import zhaofangui


class Zhaofang(unittest.TestCase):
    def setUp(self):
        self.url1= "http://portal-ehouse-java.itheima.net/#/login?redirect=%2F" #前
        self.url2= "http://manager-ehouse-java.itheima.net/#/login?redirect=%2Fhome%2Findex"#后
    def test_qiantai(self):
        #try:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(2)
            self.driver.get(self.url1)
            self.driver.maximize_window()
            self.driver.find_element_by_class_name("evenLogin").click()#登录
            self.driver.find_element_by_id("button").click()#体验项目
            self.driver.find_element_by_class_name("btns").click()#立即选购
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div/div/div[1]/div[2]/p[4]/button/span').click()#立即抢购
            self.driver.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > button > span').click()#确认抢购
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/span/span[1]/span[1]/a').click()#点击首页
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div[3]/button').click()#查看详情
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div/div/div[1]/div[2]/p[4]/span/span').click()#收藏
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/span/span[1]/span[1]/a').click()  # 点击首页
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/p/span[1]').click()# 点击欢迎您
            self.driver.find_element_by_class_name('high').click()#我的收藏
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div/p/span[1]').click()#我的订单
            self.driver.find_element_by_class_name('spec').click()#点击查看详情
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/button/span').click()#取消选购
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/p/span[2]').click()#退出登录
        #except:
            #now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #print ("前台有错误请看截图")
            #self.driver.get_screenshot_as_file("D:\\myproject\\zhaofang\\errorpic\\"+now+".png")

    def test_houtai(self):
        #try:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(2)
            self.driver.get(self.url2)
            self.driver.maximize_window()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/button/span').click()#登录
            self.driver.find_element_by_id('button').click()#体验项目
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/div[1]/div/div[1]/div/p[1]').click()#活动开售中
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/ul/li[3]').click()#已售罄
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/ul/li[1]').click()#待开售
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="addBtn"]').click()#新增活动
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys("测试楼盘")
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/input').click()#开始时间
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]/span').click()#确定
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/input').click()#结束时间
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]/span').click()#确定
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[4]/div/div/div/input').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li/span').click()#z选择楼盘
            time.sleep(2)
            #self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span').click()#确定添加楼盘
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[3]/div/button[1]/span').click()#取消


            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[2]/a/li/span').click()  # 返回首页
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/div[2]/div/div[1]/div/p[1]').click()#昨日订单数
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[2]/a/li/span').click()  # 返回首页
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/div[2]/div/div[2]/div/p[1]').click()#本月订单数
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[3]/a/li/span').click()#楼盘列表
            self.driver.find_element_by_xpath('//*[@id="addBtn"]/span').click()#新增楼盘
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys("自动化楼盘")#新增-名称
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys("来自自动化的描述")#新增-描述
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/input').send_keys("自动化地址")
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[4]/div/div/input').send_keys("99999")#均价
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[5]/div/div/input').send_keys('99')#产权年薪啊
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[6]/div/div/input').send_keys('999')#规划数
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[7]/div/div/input').send_keys('99999')#占地面积
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[8]/div/div/div/input').click()#点击楼盘类型
            self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span').click()#住宅
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[9]/div/div/div/input').click()#建筑类型
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()#塔楼
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span').click()#点击确定按钮
            #self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[4]/a/li/span').click()#点击活动列表
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[5]/a/li/span').click()#点击客户管理

            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="addBtn"]').click()#点击添加客户
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys('13245555556')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys('张张哎')# namen
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[3]/div/div/input').send_keys(
                '131729199002080721') #身份证
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[4]/div/div/input').send_keys(
                'zhangzhang11')  # 登录名
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[5]/div/div/input').send_keys(
                '北京市')  # 地址
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[2]/form/div[6]/div/div/div[2]/input').click()  # 活动

            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click() #选择活动
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span').click() #确定
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/div[6]/a/li/span').click()#f房屋认证
        #except:
            #now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #print("后台有错误请看截图")
            #self.driver.get_screenshot_as_file("D:\\myproject\\zhaofang\\errorpic\\" + now + ".png")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(zhaofangui.Zhaofang("test_qiantai"))
    suite.addTest(zhaofangui.Zhaofang("test_houtai"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义报告存放路径
    filename = 'D:\\myproject\\zhaofang\\report\\report ' + now + 'result.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件


    #123123132132

