import requests 
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.international_lst .stock_up'): 
    
    country = tag.select_one('.stock_item').text
    currency = tag.select_one('.stock_price').text
    gap = tag.select_one('.gap_wrp').text
    print(f'{country}의 환율은 {currency} 이고,\n 환율 차이는 {gap} 입니다.')