def apple(x,y):
    tot1 = 0
    tot2 = 0
    tot3 = 0
    tot4 = 0
    for i in range(x + 1):
        for j in range(y + 1):
            tot1 += arr[i][j]
    for i in range(x + 1):
        for j in range(y + 1, N):
            tot2 += arr[i][j]
    for i in range(x + 1, N):
        for j in range(y + 1):
            tot3 += arr[i][j]
    for i in range(x + 1, N):
        for j in range(y + 1, N):
            tot4 += arr[i][j]

    if tot1 == tot2 == tot3 == tot4:
        return 1
    else:
        return 0


import sys
sys.stdin = open('과수원.txt')
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
result = 0
# 일단
for a in range(N):
    for b in range(N):
        result += apple(a,b)


if result == 0:
    print(-1)

else:
    print(result)

