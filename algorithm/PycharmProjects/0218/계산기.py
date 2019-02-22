
# 왼쪽괄호는 stack 들어가면 우선순위가 가잔 낮아지니까
# 오른쪽 괄호는 stack 에 안들어감 / 오른쪽 괄호 나오면 쌓여있던 연산자들 다 집어넣기 문자열에
# 숫자는 문자열에다가 집어넣고/

# 문자열 길이만큼 돌리고
# str1 = 2+3*4/5
# stack
# str2 = 후위로 바꾼 것

str = '2+3*4/5'
stack = []
str2 = []
# for i in str1:
#     if i == type(int):
#         str2.append(i)
#     else:
#         stack.append(i)
#
# for s in range(len(stack)):
#     if stack[s] == '*' or '/':
#         str2.append(s)
#
# print(str1)


for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])
    else:
        print(str[i], end='')
while len(stack) != 0:
    print(stack.pop(), end='')