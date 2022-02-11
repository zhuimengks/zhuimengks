#coding=utf-8
import requests
import re
import urllib
from io import BytesIO
from PIL import Image


import requests
import json
import urllib

from io import BytesIO
from PIL import Image

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
url = "https://pip.itcast.cn/java"
img = requests.get(url,headers=headers)
print(img)
"""
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





"""
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print (s)
print (s.keys())
print (s["name"])
print (s["type"]["name"])
print (s["type"]["parameter"][1])
"""