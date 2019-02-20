#일단 후위연산자로 만들고 -> 어제 쓴거로 계산하게 하면 됨
data = '(6+5*(2-8)/2)'
#       6528-*2/+

ope=('+','*','-','/')
point={'(':0, '+':1, '-':1, '*':2, '/':2}
stack = []
result = []

for i in range(len(data)):
    #숫자가 나오면 result에 집어넣고
    if data[i].isdigit():
        result.append(data[i])
        # (가 나오면 일단 괄호랑 괄호 안에 있는 연산자를stack에 넣음
    elif data[i] == '(' or data[i] in ope:
        stack.append(data[i])
        # 오른쪽 괄호를 만나면, 다음 (가 나올 때까지 stack에 있던 연산자를 다 result에 집어넣기
    elif data[i] == ')':
        # stack에서 stack의 가장 마지막이 (가 아닐때까지
            while stack and stack[-1] != '(':
                opes = stack.pop()
                result.append(opes)
        #괄호가 끝났으니까 stack에 남아있던 이전꺼를 result에 넣어주고, 다시 연산자와 숫자를 받기
    else:
        # opes_2= stack.pop()
        # retult.append(opes_2)



print(opes)
print(stack)
print(result)














# for i in range(len(data)):
#     # 괄호가 있기 전에는 계속 숫자를 쌓고 있다가
#     while data[i] != '(':
#         # 연산자는 쌓아놓고 있고
#         if data[i] in ope:
#             stack.append()
#         #숫자는 계속 프린트하고
#         elif data[i] != '(' and data[i] not in ope:
#             print(data[i], end='')
#
#         #계속 숫자를 프린트하다가 )가 나오면 먼저 가장 최근꺼 출력하기
#         if data[i] == ')':
#             print(stack.pop(), end='')

