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





