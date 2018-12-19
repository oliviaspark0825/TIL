# 자연수 n이 주어졌을 때, 
#1부터 n까지 한 줄에 하나씩 출력하는 프로그램 작성하시오


# item = input("번호를 입력하세요: ")
# print(The number is +  item "\n")

# item = int(input("번호를 입력하세요: "))

# for i in range(1,item+1):
#     print(i)


# for i in range(item):
#     print(i+1)


# Q
# warn_investment_list = ["microsoft", "google", "naver","kako", "samsung", 'lg']
# print(f"경고 종목 리스트: {warn_investment_list}")
# item = input('투자종목이 무엇입니까?: ')
# if item.lower() in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다")


#Q
# colors = ['Apple', 'Banana', 'Coconut','Deli', 'Ele', 'Grape']

# for i in colors:
#     if i == 4:
#         colors.append(Ele, Orange)


# #2 리스트를 하나 더 만들어주고
# fruit = []

# for i in range(len(colors)):
#     if i in [0,4,5]:
#         pass
#     else:
#         colors.append(colors[i])

# # ANSWER 6번 돌고
# colors = ['Apple', 'Banana', 'Coconut','Deli', 'Ele', 'Grape']
# fruit = []

# deleteindex = [0,4,5]
# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)


# dictionary


ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
# semester1의 기간을 출력하세요
print(ssafy["duration"]["semester1"])
# ssafy dic 안에 들어있는 '대전 출력' // 인덱스값으로
print(ssafy["location"][1])
#daejeon의 매니저 이름 출력하시오
print(ssafy["classes"]["daejeon"]["manager"])





