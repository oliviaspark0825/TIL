'''
bfs, dfs 둘다 해봐도 됨
'''


import sys
sys.stdin = open('단지.txt')


def vil(i,j):
    global Hcnt
    if i < 0 or i >= N and j < 0 or j >= N: continue
    if arr[i][c] != 1: return
    arr[r][c] = 0
    Hcnt += 1




    dx = [-1, 1, 0,0 ]
    dy = [0, 0, -1, 1]

    que = []
    que.append((i,j))
    while que:
        # 큐에 있는거를 뽑아서 현재 좌표로 놓고 시작해야지
        x,y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N and ny <0 or ny >= N: continue
            if arr[nx][ny] == 1:
                vil(nx,ny)





N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
sol = 0
Hcnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            sol = vil(i,j)

print(sol)