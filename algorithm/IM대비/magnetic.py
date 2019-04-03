import sys
sys.stdin = open('mag.txt')
N = 7
arr = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
for i in range(N):
    judge = 0
    for j in range(N):
        if arr[j][i] == 1:
            judge = 1
        elif arr[j][i] == 2:
            if judge == 1:
                cnt += 1
            judge = 0

print(cnt)