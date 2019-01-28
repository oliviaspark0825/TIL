#str 함수 구현하기
# num = 123
# c = [0] * 10
# for i in range(len(str(num))):
#     last = []
#     last = num % 10 나머지값
#     other = num // 10
#     if other > 10:
#         x = []
#         x = other // 10
#         last.extend(str(x))
# print(last)
# print(other)


def itoa(x):
    str = list()
    count = 0
    i,y = 0, 0
    while True:
        y = x % 10 # 나눈 나머지
        str.append(chr(y + ord('0')))  # 48 + 3 = 51에 해당하는 aschi를 내놔라
        x //= 10 # 123 --> 12 # 나눈 몫
        if x == 0: break
        # i += 1
    str.reverse()
    str = "".join(str) # 문자열로 바꾸기
    return str

x = 123;
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))
str2 = str(x)
print(str2, type(str2))

# 123 % 10 - 3
# 123 //10 - 12

