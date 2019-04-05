def change(x,y,l):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for h in range(1,l+1):
        for i in range(4):
            nx = x + dx[i]*h
            ny = y + dy[i]*h
            if nx <0 or nx>=N or ny <0 or ny>=N: continue
            if arr[nx][ny] == 'H' or arr[nx][ny] == 'X':
                arr[nx][ny] = 0


import sys
sys.stdin = open('기지국.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N+1)]
    cnt = 0



    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                change(i,j,1)

            if arr[i][j] == 'B':
                change(i,j,2)

            if arr[i][j] == 'C':
                change(i, j, 3)

    for a in range(N):
        for b in range(N):
            if arr[a][b] == 'H':
                cnt += 1

    print("#{} {}".format(tc+1, cnt))
    print(arr)



