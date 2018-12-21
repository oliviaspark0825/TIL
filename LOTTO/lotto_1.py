import requests
import random
from bs4 import BeautifulSoup

numbers = random.sample(range(800, 838), 8)
# for times in range(8):
    
#     url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(times)
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, "html.parser")
#     lucky_numbers = soup.select(".nums .win .ball_645")
#     bonus_num = soup.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span").text


#     print(f"{times}회차 당첨 번호")
#     print(f"{lucky_numbers} + {bonus_num} 입니다.") 
#     # for i in lucky_numbers:
#     #     print(i.text, )
#반복가능한 객체 어디서 뽑아올 것인가


# 정답
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lucky = soup.select(".ball_645")
    print(f"{num}회차 당첨 번호")
    for i in lucky:
        # end는 일렬로 만들어주는 것, 숫자를 불러와서 i 에 하나씩 나오도록 만들기
        print(i.text, end=" ")
        #for 가 반복될 때는 = count
        count += 1
        if count == 6:
            print("+", end=" ")
        # 끝나고 엔터치면 다 나오게
    print()
    



#몇번 복권을 샀을 때 1등이 나오는가?ㅣ