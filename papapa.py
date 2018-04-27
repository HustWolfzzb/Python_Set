import re
from bs4 import BeautifulSoup
import urllib
import requests
url="http://upload-images.jianshu.io/upload_images/1491667-908d845374757aa6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"
print(url)
with open('/Users/zhangzhaobo/program/python/image/11.jpg', 'wb') as f:
         f.write(requests.get(url).content)
        


