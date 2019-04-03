def ladder(x,y):
    dx = [0, 0, -1]
    dy = [1 ,-1, 0]
    while True:
        if x == 0:return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx >=100 or ny <0 or ny >=100: continue
            if arr[nx][ny] == 0: continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 9
                x = nx
                y = ny


import sys
sys.stdin = open('ladder.txt')
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    sx = 99
    ans = 0
    for i in range(100):
        if arr[sx][i] == 2:
            ans = ladder(sx,i)


    print("#{} {}".format(tc+1, ans))