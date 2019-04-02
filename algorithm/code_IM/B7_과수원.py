def apple(x,y):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for a in range(x+1):
        for b in range(y+1):
            s1 += arr[a][b]

    for a in range(x+1, N):
        for b in range(y+1):
            s2 += arr[a][b]

    for a in range(x+1):
        for b in range(y+1,N):
            s3 += arr[a][b]

    for a in range(x+1, N):
        for b in range(y+1, N):
            s4 += arr[a][b]

    if s1 == s2 == s3 == s4:
        return 1
    else:
        return 0

import sys
sys.stdin = open('과수원.txt')
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# 자르는 기준을 i, j 라고 하면
tot = 0
for i in range(N):
    for j in range(N):
        tot += apple(i,j)


if tot == 0:
    print(-1)
else:
    print(tot)