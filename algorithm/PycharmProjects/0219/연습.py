def iswall(r, c):
    global N, arr
    if r<0 or r>=N:
        return True
    if c<0 or c>=N:
        return True
    return False


def maze(x, y):
    global arr, result
    dx = [-1, 0, 1, 0] # 위 오른 아래 왼
    dy = [0, 1, 0, -1]

    for i in range(4):
        if iswall(x+dx[i], y+dy[i]) == False and arr[x+dx[i]][y+dy[i]] !=1:   # 벽이 아니면
            if arr[x+dx[i]][y+dy[i]] == 3:
                result = 1
            #print(x,y)
            arr[x][y] = 1
            maze(x+dx[i], y+dy[i])

import sys
sys.stdin = open('미로.txt')
T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)
    result = 0
    r = 0  # 시작점 찾기 (2)
    c = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                r = row
                c = col
                break
    maze(r, c)

    print('#{} {}'.format(t+1, result))
    #print('Rmx')