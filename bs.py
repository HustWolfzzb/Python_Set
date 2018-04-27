from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.jianshu.com")
bsObj = BeautifulSoup(html)
print(bsObj.h1)
nameList=bsObj.findAll("h4",{"class":"title"})
information=bsObj.findAll("div",{"class":"list-footer"})
for name,info in nameList,information:
        print(name.get_text())
        print(info.get_text())

