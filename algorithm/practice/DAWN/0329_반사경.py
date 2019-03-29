def reflect(x,y):


import sys
sys.stdin = open('반사경.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
 # 0 빈공간, 1 방향 1거울 2 방향 2거울
    sx,sy, dir = 0, 0, 0
    dx = [0, 1, 0, -1] # 오 아 왼 위
    dy = [1, 0, -1, 0]
    for x in range(N):
        for y in range(N):
            if x <0 or x >=N or y <0 or y >=N: print(cnt)
            if data[x][y] == 2 and
                dir = dx[1]

