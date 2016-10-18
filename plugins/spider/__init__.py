# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.wkzf.com/shanghai/esf/p1")
soup = BeautifulSoup(res.content)
for s in soup.select(".ulcenter ul"):
    print s

res = requests.get("http://www.wkzf.com/shanghai/esf/detail/3537d8348a0c8f6a.html")
soup = BeautifulSoup(res.content)
for s in soup.select(".w-oldhousehead"):
    print s
