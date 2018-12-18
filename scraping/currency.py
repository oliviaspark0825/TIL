# import requests 
# from bs4 import BeautifulSoup
# #요청해서 변수에 담고 응답받고 #예쁘게 꾸며서 soup에 넣어줌 # 딱 하나만 찝어내서 불러오기
# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# # text만 불러와야하니까
# print(kospi.text)


# import requests 
# from bs4 import BeautifulSoup
# #요청해서 변수에 담고 응답받고 #예쁘게 꾸며서 soup에 넣어줌 # 딱 하나만 찝어내서 불러오기
# req = requests.get("http://www.wemakeprice.com/deal/adeal/4226254/100600/?source=mdeal&tab=&no=9").text
# soup = BeautifulSoup(req, 'html.parser')
# price = soup.select_one("#contents > div.content-main > div.deal_area > div > div.price_area.app.new > div.price_info.wprice > div.set_price_area > ul > li.sale > span.num")
# # text만 불러와야하니까
# print(price.text)


# import requests 
# from bs4 import BeautifulSoup
# #요청해서 변수에 담고 응답받고 #예쁘게 꾸며서 soup에 넣어줌 # 딱 하나만 찝어내서 불러오기
# req = requests.get("https://www2.hm.com/ko_kr/favourites").text
# soup = BeautifulSoup(req, 'html.parser')
# name = soup.select_one("body > header > div.wrapper > div.top-strip > nav.services-menu > div.linklist1.linklist.parbase > ul > li:nth-child(2) > a")
# # text만 불러와야하니까
# print(name.text)


#네이버 실시간 검색어 스크래핑
# import requests 
# from bs4 import BeautifulSoup

# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# ah = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div")

# for i in ah:
#     i = soup.select("li class= ah_item")
# print(i.text)

#for i in ah: 
    #i = select()
    #for i in ah:
#    i = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")



#네이버 답안
import requests 
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'): 
    
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name} 입니다.')
#.PM_CL_realtimeKeyword_rolling
