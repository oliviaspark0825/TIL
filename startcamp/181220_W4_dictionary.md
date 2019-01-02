# 181220_W4_dictionary

```python
"""
파이썬 dictionary 활용 기초!
"""
#  for문에서 반복적으로 값을 가져오려고 할 때
dict = {
    "대전": 23,
    "서울": 30,
    "구미": 20
}
print(type(dict.values()))
#range가 반복 가능한 객체(iterator) 나 dict이나 같음
#type: 무슨 타입인지 보여주는 것

list = [1,231,"123132"]
print(len(list))
#list : 안의 요소의 갯수가 몇 개인지 보여주는 것
```

```python
# 1. 평균을 구하세요.
#1-1 ans
scores ={
    "국어": 87,
    "영어": 92,
    "수학": 40
}
# 빈 변수를 하나 만들어야 함
# total score = total_score + score => +=score // 변수를 갱신시키는 것
total_score = 0 
for score in scores.values():
    total_score += score
# len 값이 3이니까
average_score = total_score / len(scores)
print(average_score)


# 1-2 ans
total_score = sum(scores.values())
average_score = total_score / len(scores)
```

```python
# 2 ans
# dict이 여러단계니까 단계씩 한칸씩 들어가기
# for문이 돌아가니까 숫자를 한번씩 세면 총 6번이 되겠지? 0을 할당한다음에 돌아가는 횟수를 세는거
#2. 반 평균을 구하시오
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}




total_score = 0
count = 0
for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score += indivisual_score
        count += 1

average_score = total_score / count
print(average_score)
# print(total_score)
```

```python
scores = {
     "철수": {
         "수학": 80,
        "국어": 90,
         "음악": 100
}
}
for key, value in scores.items():
    print(key)
    print(value)
// for문으로 키랑 밸류값 가지고 오는 방법
```



최고최저온도

```python
# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
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

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가  cold 보다 더 추우면, cold  에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot 보다 더 더우면, hot  에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")
```



```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
파이썬 껐다 켰다
```

 