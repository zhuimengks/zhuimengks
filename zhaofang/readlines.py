from selenium import  webdriver
import  time
import xlrd
def excel():
    wb = xlrd.open_workbook("E:\\wangzhi\\wangzhi.xls",'rb')# 打开Excel文件
    sheet = wb.sheet_by_name('becks')#通过excel表格名称(becks)获取工作表
    dat = []  #创建空list

    for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                data1 = cells[0]
                dat.append(data1)
                #data=int(cells[1])#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
                #dat.append(cells) #把每次循环读取的数据插入到list
                #dat.append(data)

    return dat

a = excel() #返回整个函数的值
print (a)

"""def test(a):
    for b in a:
        print(b)
        c = b[0]#取值
        driver = webdriver.Chrome()
        driver.maximize_window()
        s1 = time.time()
        driver.get(c)
        time.sleep(3)
        s2 = time.time()
        print(s2 - s1 - 3)
        time.sleep(3)
        driver.quit()
test(a)




class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
"""