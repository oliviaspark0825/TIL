import sys
sys.stdin = open('워크샵.txt', 'r')
for tc in range(10):
    T = int(input())  # 텍스트 길이
    data = input()# split 쓰면 공백을 기준으로 나누는건데, 지금 공백 없으니까
    print(T)
    print(data)
    stack = []
    # for i in range(len(data)):
    #     if data[i] == '(':
    #
    #     if data[i] == '+' or data[i] =='-' or data[i] == '*' or data[i] =='/':
    #         stack.append(data[i])
    # print(stack)


 #먼저 괄호를 빼내면서 / 사이에 있는 숫자를 다 stack에 저장하고, 연산자를 붙인다음에 /
 #오른쪽 괄호가 나올때까지 빼내기
 일단 숫자를 만나면