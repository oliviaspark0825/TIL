def maze(y, x):
    global N, flag
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
#시작점을 찾으면 -방문처리하고 - 인접한 정점중 방문안하거를 가지고 dfs
    data[y][x] = 9 #방문표시
#4 방향을 가야하니까
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
#벗어나면 오류나니까, index를 먼저 넣어주고 체크하기
        if ny < 0 or ny == N: continue
        if nx < 0 or nx == N: continue
        if data[ny][nx] == 9 : continue
        if data[ny][nx] == 1 : continue
        if data[ny][nx] == 3:
            #원하는데 도착한거니까 그만하라
            flag = 1
            return
        maze(ny, nx)


def findStart(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x

import sys
sys.stdin = open('미로_input.txt', 'r')
T = int(input())
for tc in range(T):
    #재귀라서 - 재귀는 리턴하기 힘들어서 flag 쓰는거임
    flag = 0
    N = int(input())
    data = [[int(x) for x in input()] for _ in range(N)]  # 미로를 중첩리스트로 저장
    # data = [0 for _ in range(N)]
    # for i in range(N):
    #     data[i]
    visit = [[0 for _ in range(N)]for _ in range(N)]

#시작 포인트를 주고 시작
    sy, sx = findStart(data)
    maze(sy, sx)
    print(f"#{tc+1} {flag}")
