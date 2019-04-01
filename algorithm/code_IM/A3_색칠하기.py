
import sys
sys.stdin = open('a3색칠하기.txt')
Y,X,N = list(map(int,input().split())) # 세로 가로 바뀜
arr = [[0]*20 for _ in range(20)]
# 일단 처음꺼는 집어넣고
sx1,sy1,ex1,ey1,degree1 = list(map(int,input().split()))

check = degree1
for i in range(sx1, ex1+1):
    for j in range(sy1, ey1+1):
        arr[i][j] = degree1
        check =degree1
        maxx = check
for a in range(N-1):
    sx, sy, ex, ey, degree = list(map(int,input().split()))
    # sx, sy, ex, ey, degree = [list(map(int, input().split())) for _ in range(N-1)]
    for s in range(sx, ex+1):
        for k in range(sy, ey+1):
            if arr[s][k] > degree:
                break
            else:
                arr[s][k] = degree
                check = degree
                if check > maxx:
                    maxx = check

tot = 0
for p in range(20):
    for q in range(20):
        if arr[p][q] == maxx:
            tot += 1

print(tot)





#
# square = [list(map(int,input().split())) for _ in range(N)]
# check = square[0][4]
# for i in range(square[i][0], square[i][2]+1):
#     for j in range(square[j][1], )

