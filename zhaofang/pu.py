import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://pip.itcast.cn/home")
try:
    driver.find_element_by_id("is")

except:
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print ("前台有错误请看截图")
    driver.get_screenshot_as_file("D:\\myproject\\zhaofang\\errorpic\\ " +now +".png")
