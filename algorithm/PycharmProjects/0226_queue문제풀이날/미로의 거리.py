def bfs(x,y):
    global G, V
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue=[]
    #queue에다가 좌표를 저장
    queue.append([x,y])  #enQueue하면서 방문처리
    visited[x][y] = 1 #방문한 행렬좌표 값을 1로 처리하기
    # print(v, end=" ")
    while len(queue) != 0:
        t = queue.pop(0)
        #방문한 행렬좌표 t = [x,y] pop
        for w in range(4):
            nx = t[0] + dx[w]
            ny = t[1] + dy[w]
            if ny < 0 or ny == N: continue
            if nx < 0 or nx == N: continue
            if data[nx][ny] == 3:
                visited[nx][ny] = visited[t[0]][t[1]]
                return visited[nx][ny] -1
            if data[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[t[0]][t[1]] + 1
                queue.append([nx,ny])
                             # 경로가 없는 경우 == 0
    return 0

def findStart(data):
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y

import sys
sys.stdin = open('미로의 거리.txt', 'r')
T = int(input())
for tc in range(T):
    N = int(input())
    # split을 할 공백이 없으니까 13101을 통째로 받아서 문제였던거임
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 시작점 찾기
    sx, sy = findStart(data)
    ans = bfs(sx, sy) # 시작점에서부터 bfs 시작

    print(f"#{tc + 1} {ans}")
