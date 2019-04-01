import sys
sys.stdin = open('수열2.txt')
N = int(input())
arr= [list(map(int,input().split())) for _ in range(N)]
maxx = -9876
# 증가
for i in range(N):
    cnt = 1
    for j in range(N-1):
        if arr[i][j+1] == arr[i][j] +1:
            cnt +=1

    if cnt > maxx:
        maxx = cnt

#감소하는 수열
for i in range(N):
    cnt = 1
    for j in range(N - 1):
        if arr[i][j+1] == arr[i][j] -1:
            cnt += 1
    if cnt > maxx:
        maxx = cnt

########## 세로 ##########
for j in range(N):
    cnt = 1
    for i in range(N-1):
        if arr[i+1][j] == arr[i][j] +1:
            cnt +=1

    if cnt > maxx:
        maxx = cnt

#감소하는 수열
for j in range(N):
    cnt = 1
    for i in range(N-1):
        if arr[i+1][j] == arr[i][j] -1:
            cnt += 1
    if cnt > maxx:
        maxx = cnt


print(maxx)