# import sys
# sys.stdin = open('대각선.txt')
T = int(input())
for tc in range(T):
    N, K = list(map(int,input().split()))
    fruit = [list(map(int,input().split())) for _ in range(N)]
sum_right = 0
sum_left = 0
leftside = []
rightside = []
# 왼쪽 대각선 합 구하기
# x, y 좌표가 1씩 증가
for i in range(N):
    for j in range(i+3):
        if i<0 or i >= N: continue
        if j<0 or j >= N: continue
        sum_left  += fruit[i][j]
        i += 1
        if i == N:
            break
    leftside.append(sum_left)

#오른쪽 대각선 합 구하기
# x 좌표는 1씩 증가 y 좌표는 1씩 감소
for i in range(N):
    for j in range(K,0,-1):
        if i<0 or i >= N: continue
        if j<0 or j >= N: continue
        sum_right += fruit[j][j]
        i += 1
        if i == K:
            break
    rightside.append(sum_right)

# 각 대각선 합의 차의 최소 구하기
total = []
for i in range(N):
    if leftside[i] > rightside[i]:
        total.append(leftside[i] - rightside[i])
    else:
        total.append(rightside[i] - leftside[i])

print("#{} {}".format(tc+1,min(total)))
