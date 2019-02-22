def dfs(x, y):
# 현재좌표와, 4방향 좌표를 만들어서 이동시키기
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

for i in range(4):
    nx = x + dx[i]
    ny = y + dx[i]
    if check():
        data[nx][ny] = 9

dfs(nx, ny)





