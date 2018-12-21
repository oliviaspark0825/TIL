import requests
import json
import os 
from bs4 import BeautifulSoup

"""
#처음에 했던 것
# token = "770993571:AAH2fqhmCo_Khf_60FsgmSffkHj2vB680E8"
# # method_name = "getUpdates"
# # url = f"https://api.telegram.org/bot{token}/{method_name}"
# chat_id = 753172166


# msg = "안녕하세요 ㅎㅎ"
# method_name = "sendmessage"
# msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={753172166}&text={msg}"

# print(msg_url)
# print(requests.get(msg_url))

"""

#환경변수 설정
token = os.getenv("TELEGRAM_BOT_TOKEN")
# method_name = "getUpdates"
# url = f"https://api.telegram.org/bot{token}/{method_name}"
# chat_id = 753172166
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
update = requests.get(url).json()
chat_id = update["result"][0]["message"]["from"]["id"]

# # list는 순서가 정해져 있는데, 지금 전체가 한 덩어리하서  [0]이렇게 한거임, 


url_cos = "https://finance.naver.com/sise/"
req = requests.get(url_cos).text
soup = BeautifulSoup(req,'html.parser')

kospi = soup.select_one('#KOSPI_now').text
method_name = "sendmessage"
msg = f"오늘의 코스피지수는 {kospi} 입니다. "
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"

print(msg_url)
print(requests.get(msg_url))






