def catch(x,y):
    dx = [-1,-2, 1, 2, 2, 1, -1, -2] # 오2위1 오1위2 오2아래1 오1아래2
    dy = [2, 1, 2, 1, -1, -2, -2, -1] # 왼1아래2 왼2아래1 왼2위1 왼1위2

    que = []
    que.append((x,y,0))
    arr[x][y] = 1
    while que:
        x, y, time = que.pop(0)
        if x == ex and y == ey:
            return time
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= X or ny <0 or ny >= Y: continue
            if arr[nx][ny] !=1:
                que.append((nx,ny,time+1))
                arr[nx][ny] =1
    return -1







import sys
sys.stdin = open('장기.txt')
X,Y = list(map(int,input().split()))
sx,sy, ex,ey = list(map(int,input().split()))
arr = [[0 for _ in range(Y)] for _ in range(X)]

sx -=1; sy -=1; ex -=1; ey -=1;
answer = catch(sx,sy)
print(answer)