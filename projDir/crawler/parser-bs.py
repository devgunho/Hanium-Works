import requests
import re
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('http://www.gukbi.com/Academy/')

# HTML 소스 가져오기
html = req.text

# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')

crawlData = []
saveIndex = []

for pTag in soup.find_all('p'):
        crawlData.append(pTag.text)
for index, value in enumerate(crawlData):
        if value == 'IT/정보통신/컴퓨터':
                saveIndex.append(index)
                
for i in range(len(saveIndex)):
        print(crawlData[saveIndex[i]+1])
        print(crawlData[saveIndex[i]+2])
        print(crawlData[saveIndex[i]+3])
        print("----------------------------")