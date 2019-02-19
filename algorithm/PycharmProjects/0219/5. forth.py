import sys
sys.stdin = open('forth.txt', 'r')
T = int(input())
for tc in range(T):
    data = input().split()

    stack = []
    ope = '+-/*'
    result = ''
    for i in range(len(data)):
        # 1) 숫자만 stack에 넣기
        if data[i] not in ope and data[i] != '.':
            stack.append(data[i])

        # 2) 연산자인 경우
        elif data[i] in ope:
            if len(stack) < 2:# 숫자가 1개일 경우 에러
                result ='error'
                break
            else: # 숫자가 2개이상일 경우 각 연산자에 맞추어 계산
                if data[i] == '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n1) + int(n2))
                    result = stack[-1]

                elif data[i] == '-':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2) - int(n1))
                    result = stack[-1]

                elif data[i] == '/':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2) // int(n1))
                    result = stack[-1]
                elif data[i] == '*':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2) * int(n1))
                    result = stack[-1]

        elif data[i] == '.':
            if len(stack) >=2:
                result = 'error'# . 일경우는 끝내기
                break
    print(f'#{tc+1} {result}')
