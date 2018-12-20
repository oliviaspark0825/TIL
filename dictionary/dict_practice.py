"""
파이썬 dictionary 활용 기초!
"""

# for i in range(3):
#     int i = score.values
#     x = sum(i)
# average = x/3

# 1. 평균을 구하세요.
#1-1 ans
# scores ={
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }
# # 빈 변수를 하나 만들어야 함
# # total score = total_score + score => +=score // 변수를 갱신시키는 것
# total_score = 0 
# for score in scores.values():
#     total_score += score
# # len 값이 3이니까
# average_score = total_score / len(scores)
# print(average_score)


# # 1-2 ans
# total_score = sum(scores.values())
# average_score = total_score / len(scores)



# dict = score
# total = sum(dict.values())
# print(total/3)

# dict = score
# for i in range(3):
#     total = (dict.values(i))
# average = total/len(dict)
# print(average)

# dict.values(score)

# #2. 반 평균을 구하시오
# scores = {
#     "철수": {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "영희": {
#         "수학": 70,
#         "국어": 60,
#         "음악": 50
#     }
# }

# total_score = 0
# for name in scores:
#     for score in scores[name].values():
#         total_score += score

# number = len(sum(scores[name].values))
# print(number)
# # average_score = total_score/number
# # print(average_score)

# 2 ans
# dict이 여러단계니까 단계씩 한칸씩 들어가기
# for문이 돌아가니까 숫자를 한번씩 세면 총 6번이 되겠지? 0을 할당한다음에 돌아가는 횟수를 세는거

# total_score = 0
# count = 0
# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# average_score = total_score / count
# print(average_score)
      # print(total_score)




# scores = {
#      "철수": {
#          "수학": 80,
#         "국어": 90,
#          "음악": 100
# }
# }
# for key, value in scores.items():
#     print(key)
#     print(value)

#3 도시중에 최근 3일 중 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0
# 정답

for name,temp in cities.items():
   #name = "서울"
   #temp = [-6, -10, 5] // 처음에 불러오는 값이겠지?
    if count == 0:
       hot = max(temp)
    #지금 서울이 들어가있엤지, 그리고 무조건 처음에 서울의 값이 드어가야하니까  true가 필요함
       cold = min(temp)
       hot_city = name
       cold_city = name
    else:
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
       # 하나가더해져서 대전이 들어옴 최저온도가 cold(서울)보다 더 추우면 cold가 갱신되어야겠지? / 바뀌어야겠지?
       #최고 온도가 hot 보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1
print(f"{hot_city},{cold_city}")





    




