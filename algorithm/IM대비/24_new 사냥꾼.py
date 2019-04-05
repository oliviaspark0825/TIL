def hunt(x,y):
    dx = [-1,-1, 0, 1, 1, 1, 0,-1]
    dy = [0, 1, 1, 1, 0,-1, -1,-1 ]

    for i in range(8):
        for h in range(1, N):
            nx = x + dx[i]*h
            ny = y + dy[i]*h
            if nx<0 or nx >=N or ny<0 or ny>=N: continue
            if arr[nx][ny] == 0: break # 사냥꾼이면
            if arr[nx][ny] == 1: break
            if arr[nx][ny] == 2:
                arr[nx][ny] = 9




import sys
sys.stdin = open('new사냥.txt')
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
print(arr)
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hunt(i,j)

for a in range(N):
    for b in range(N):
        if arr[a][b] == 9:
            cnt += 1

print(cnt)

