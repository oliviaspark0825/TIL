def ladder(x,y):
  # 탈 때마다 체크
    cnt = 0
    visit = [[0] * 100 for _ in range(100)]
    visit[x][y] = 1
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    while True:
        if x ==99: return cnt
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=100 or ny <0 or ny >= 100: continue
            if arr[nx][ny] == 0: continue
            if visit[nx][ny] == 1: continue
            if arr[nx][ny] == 1:
                visit[nx][ny] = 1
                cnt += 1
                x = nx
                y = ny




import sys
sys.stdin = open('lad2.txt')
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    minn = 9876543
    tot = []
    ans = 0
    sx = 0
    for i in range(100):
        if arr[sx][i] == 1:
            tot.append((ladder(sx,i),i))

    for i in range(len(tot)):
        if tot[i][0] < minn:
            minn = tot[i][0]

    for s in range(len(tot)):
        if tot[s][0] == minn:
            ans = tot[s][1]

    print("#{} {}".format(tc+1, ans))