def find(x,y):
    dr = [0,-1, 1, 0, 0]
    dc = [0,0, 0, -1, 1]
    dno = 0
    r, c = x
    check = 9
    cnt = 0
    r = r + dr[direction[dno]]
    c = c + dc[direction[dno]]
    if map[r][c] == 0:
        map[r][c] = check
        cnt += 1

    elif map[r][c] == 1:
        r -= dr[direction[dno]]
        c -= dc[direction[dno]]
        dno += 1
        if dno == 4:
            dno = 0
    else:
        break

import sys
sys.stdin = open('구슬굴리기.txt')
N,N = list(map(int,input().split()))
map = [list(map(int,input())) for _ in range(N)]
way = int(input())
direction = [int(i) for i in input().split()]

# 일단 2인 지점에서 시작하기
for i in range(N):
    for j in range(N):
        if map[i][j] == 2:
            find(i,j)




print(cnt)



