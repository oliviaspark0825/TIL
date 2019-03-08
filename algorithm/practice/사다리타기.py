def ladder(x,y):
    global arr, visited
    visited = [[0 for _ in range(100)] for _ in range(100)]
    dx = [0, 1, 0 ]
    dy = [1, 0, -1]
    #일단 처음 값이 1인거 찾았으면 방문표시하고 시작
    visited[x][y] = 1
    while nx != 99:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 행의 인덱스가 99가 아닌 동안

            if nx < 0 or nx >= 100: continue
            if ny < 0 or ny >= 100: continue
            if arr[nx][ny] == 0: continue
            # 우리가 찾는 마지막 행의 1번일 경우
            if arr[nx][ny] == 1 and nx == 99:
                return visited[x][y] -1
            elif arr[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
    return 0

import sys
sys.stdin = open('사다리타기.txt')
T = int(input())
for tc in range(T):
    arr = [list(map(int,input().split())) for _ in range(100)]

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            distance = ladder(i,j)

print(distance)