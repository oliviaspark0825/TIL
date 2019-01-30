import requests
from bs4 import BeautifulSoup
# req = requests.get("https://www.google.com").text
url = 'https://finance.naver.com/sise/'
req = requests.get(url).text 
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now') # 경로써주기

print(kospi.text) # text로 해야 html 안에있는게 숫자로 나오게 됨
# 자체를 텍스트로 바꾸기
# print(req)
# print(req.text)
# print(req.status_code)

# soup = BeautifulSoup.(req, 'html.parser') # beautifulsoup이 읽을 수 있도록 
# kospi = soup.select_one('경로')
# print(kospi.text)
