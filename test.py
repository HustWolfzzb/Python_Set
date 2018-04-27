import requests
#from bs4 import BeautifulSoup
from lxml import etree
header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Connection":"keep-alive",
"Cookie":"Hm_lvt_c1f5ca77be259d6b1faf0ca1330f8532=1501001268; remember_user_token=W1szODEwNzc1XSwiJDJhJDEwJDVHRlAxYzRvUHNyem82MFFtRFkvOC4iLCIxNTEwODg3MDE5Ljc3NzYwOTgiXQ%3D%3D--95ea5dd90c17899c1f5b7cc2748d056b8ebee27c; read_mode=day; default_font=font1; _gat=1; locale=zh-CN; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223810775%22%2C%22%24device_id%22%3A%2215f2e6e98654c6-0b5c95c7db18d6-31657c00-1296000-15f2e6e9866726%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-banner-s%22%2C%22%24latest_utm_campaign%22%3A%22maleskine%22%2C%22%24latest_utm_content%22%3A%22note%22%7D%2C%22first_id%22%3A%2215f2e6e98654c6-0b5c95c7db18d6-31657c00-1296000-15f2e6e9866726%22%7D; _ga=GA1.2.1842248919.1484722514; _gid=GA1.2.1370677840.1510620964; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1511429503,1511433158,1511441135,1511441790; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1511443794; _m7e_session=06b7ffc0632a5888dce80cc22a6aba67",
"Host":"www.jianshu.com",
"Referer":"http://www.jianshu.com/u/9142b2802fa2",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


html = requests.get("http://www.jianshu.com/u/9142b2802fa2",headers=header)
tree=etree.HTML(html.content)
for x in tree.xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[2]/div"):
    print(x.xpath("a/p/text()"))

