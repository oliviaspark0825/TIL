import random
import requests
import json
from pprint import pprint
"""
0.random 으로 로또 번호를 생성합니다. (내가 살 번호)
1. api를 통해 우승 번호를 가져옵니다. (1주일에 한번)
2. 0번과 1번을 비교하여 나의 등수를 알려준다.
---------------
1. url 요청 보내서 정보를 가져옵니다
    -json으로 받는다. (딕셔너리로 접근 가능)
2. api의 당첨번호와 보너스 번호를 저장하고,
3. 뽑은게 몇 등인지 하는거 뽑으세요. 
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()
"""


# url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# site_nums = []
# bonus_num = [(lotto["bnusNo"])]

# for i in range(1,7):
#     single_num = lotto.get(f"drwtNo{i}")
#     site_nums.append(single_num)



# same = 0
# second_same = 0
# count = 0

# while same < 7:
#     my_nums = random.sample(range(0,46),6)
#     same = (len(set(my_nums) & set(site_nums)))
#     second_same = (len(set(my_nums) & set(bonus_num)))
#     count += 1

    
    #if same == 3:
        #print(f"5등에 당첨되셨습니다.")
    
    #if same == 4:
       # print(f"4등에 당첨되셨습니다.")
    
    
    #if same == 5:
   #     print(f"3등에 당첨되셨습니다.")
#    #     if second_same == 1:
#    #         print(f"2등에 당첨되셨습니다.")
#     if same == 6:
#         print(f"운이 좋으시군요. 1등입니다.")
#         same = 8

# print(f"도전 횟수는 {count}입니다.")




# for i in numbers : 
#   if i == list 
# # print(lotto)

# pprint(lotto)
# print(type(lotto))
# 여기까지 불러온거, 앞으로 제이슨으로 불러옴


    # lucky = soup.select(".ball_645")
    # print(f"{num}회차 당첨 번호")
    # for i in lucky:



url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1,7):
    winner.append(lotto[f"drwtNo{i}"])
# 1부터 6까지 해당되는 값을 불러 오는 것
# 837회차 번호가 winner에 들어옴
bonus = lotto["bnusNo"]
#print(bonus) 중간중간 계속 찍어보기
print("이번 주 당첨 번호:" + str(winner))
print("보너스 번호: " + str(bonus))
count = 0

while True:
    count += 1
    # 몇번 째 되었는데 알고 싶을 경우
    # 내 번호는 계속 생성되어야하니까  while 안에 들어와져있어야 함
    my_numbers = sorted(random.sample(range(1,46),6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등")
    elif  matched ==5:
        if bonus in my_numbers:
            # 5개 맞고 들어온 상태
            print("2등")
        else:
            print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ',')
        print("쓴 돈은", money)
        # print(count *1000, "원 써서 먹었습니다.")
        break

    else:
        print(" 응 안돼")
# CTRL + D  DDDD 이름을 한번에 바꾸고 싶을때
# ALT + 화살표 위아래하면 줄이 서로 바꿈
# 다 드래그 하고 SHIFT 누르면 한번에 INDENT 됨
# ALT + CTRL
