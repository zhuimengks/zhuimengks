import requests
import re
import urllib
from io import BytesIO
from PIL import Image
#搜狗图片下载-接口类
#coding=utf-8

import requests
import json
import urllib
"""
def getSogouImag(category,length,path):
    n = length
    cate = category
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        #imgs_url.append(j['ori_pic_url'])#原始图片
        imgs_url.append(j['bthumbUrl'])#缩略图
    m = 0
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
    print('Download complete!')

getSogouImag('壁纸',2000,'d:/download/壁纸/')



#百度花草类别图片下载-接口类
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7897578739120035239&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E8%8A%B1%E8%8D%89&queryWord=%E8%8A%B1%E8%8D%89&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=120&rn=120&gsm=1e&1640220695480="
img = requests.get(url,headers=headers)
print(img)
jd = json.loads(img.text)
imgs = []
for numbers in range(1,29):
    #print(numbers)
    #print(jd['data'][numbers]['hoverURL'])
    imgs.append(jd['data'][numbers]['hoverURL'])
print(imgs)
m =0
path = r"D:\pictures\pictures"
for img in imgs:
    print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
    urllib.request.urlretrieve(img, path + str(m) + '.jpg')
    m =m+1
print('Download complete!')
"""
#js提取样例可以帮助理解js的数据提取
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print (s)
print (s.keys())
print (s["name"])
print (s["type"]["name"])
print (s["type"]["parameter"][1])



