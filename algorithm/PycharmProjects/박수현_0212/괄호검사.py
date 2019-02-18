# 괄호검사
import sys
sys.stdin = open("괄호검사.txt")
T = int(input())

for tc in range(T):
    data = input()

    phr = ''
    check = '{}()'
    for i in data:
        if i in check:
            phr += i
    # print(phr)
    cnt = 0
    for s in phr:
        if s == '{':
            cnt += 1
        elif s == '}':
            cnt -= 1
        elif s == "(":
            cnt += 2
        elif s == ")":
            cnt -= 2
    if cnt == 0:
        print('#{} {}'.format(tc+1, 1))
    else:
        print('#{} {}'.format(tc + 1, 0))



# {{ 왼쪽거는 append 하고 오늘쪽은 같은지 비교하고 pop 하기, 만약 0 이면 바로 빠져나오게 하고

