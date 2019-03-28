ey = 0
ex = 0

def find(x,y):
    global ey, ex

    que = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    que.append((x,y,0))
    # 내가 숫자를 받은거가 가로 세로 반대로 받았는데, 원래 배열 자체에서는 무조건
    # 가로가 먼저 세로가 다음으로 받으니까 바꿔서 주어야 함
    arr[y][x] = 1 # 방문표시
    while que:
        x,y, time = que.pop(0)
        if x == ex and y == ey:
            return time
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if arr[ny][nx] == 1: continue
            if nx<0 or nx >= Y or ny < 0 or ny >=X: continue
            if arr[ny][nx] == 0:
                que.append((nx,ny,time+1))
                arr[ny][nx] =1
    return -1




import sys
sys.stdin = open('미로탈출로봇.txt')
X,Y = list(map(int,input().split()))
sx,sy,ex,ey = list(map(int,input().split()))
arr = [list(map(int,input())) for _ in range(Y)]
sx -= 1 ;sy -= 1; ex -=1; ey -= 1

rst = find(sx,sy)

print(rst)