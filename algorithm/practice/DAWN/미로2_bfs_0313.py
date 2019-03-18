'''
BFS -  q를 만들어 쌓기
'''

def bfs(x,y):
    Q.append((x,y)) # 튜플 형태로 집어넣기
    visited[x][y] = 1
    while len(Q) != 0:
        x,y = Q.pop(0)
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        for i in range(4):
            nx = x + dx[i]
            ny = y +dy[i]
            #벽체크하기
            if nx <0 or nx >= 100: continue
            if ny < 0 or ny >= 100: continue
            if visited[nx][ny] == 1: continue
            if data[nx][ny] == 1: continue
            if data[nx][ny] == 3:
                return 1

            if data[nx][ny] == 0:
                Q.append((nx,ny))
                visited[nx][ny] = 1
                # 도착지이면 리턴하라

    return 0










import sys
sys.stdin = open('미로2.txt')
T = 10
for tc in range(T):
    N = int(input())
    data = [list(map(int,input())) for _ in range(100)]

    # data = [0 for _ in range(100)]
    for i in range(100):
        data.append(input())


    # for i in range(100):
    #     # 문자열로 받을때
    #     # data[i] = list(input())
    #     # 숫자로 받을 때
    #     data[i] = list(map(int,input()))

    # data = [[int(x) for x in input()] for _ in range(100)]

    Q = []
    visited = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if data[i][j] == 2:
                result = bfs(i,j)
    print('#{} {}'.format(tc+1, result))