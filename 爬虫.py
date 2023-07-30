import requests
from lxml import etree
from urllib.request import urlretrieve

url = 'https://www.bilibili.com/read/cv19596192'

# //*[@id="read-article-holder"]/figure[2]/img
# //*[@id="read-article-holder"]/figure[10]/img
# //*[@id="read-article-holder"]/figure[101]/img


requests = requests.get(url)
if requests.status_code == 200:
    print("请求成功")
    response = requests.text
    HTML = etree.HTML(response)
    figures = []
    for x in range(2, 102):
        figures.append(HTML.xpath('//*[@id="read-article-holder"]/figure[%d]/img/@data-src' % x))
    srcs = []
    for src in figures:
        src= src[0]
        if src[0] == "/":
            src = "https:" + src
        srcs.append(src)
    print(srcs)
else:
    print("请求失败")

i = 0
for src in srcs:
    i += 1
    urlretrieve(src, f"./images/{i}.png")
