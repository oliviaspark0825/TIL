#문자열 숫자를 정수로 변환하기
#문자로 비교할때는 아스키 코드로 비교해야함
def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9': #맨 앞 숫자
            digit = ord(c) - ord('0') # 아스키 코드 번호로 바꾸는 함수가 ord - 1:45 = 빼면 숫자가 나오니까

        else:
            break # 0이면 나가리게
        value = (value * 10) + digit; # 계속 10이랑 곱해서 자릿수를 만들어서
        i += 1
    return value

a= '123A'
print(type(a))
b = atoi(a)
print(type(b))
# c = int(a)
# print(type(c))