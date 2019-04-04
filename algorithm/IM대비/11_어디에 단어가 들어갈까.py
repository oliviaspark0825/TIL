import sys
sys.stdin = open('단어.txt')
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    tot = 0
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 막힌 곳이나 이미 방문을 한 자리이면 지나가고
            if arr[i][j] == 0 or visit[i][j] == 1: continue
            cnt = 0
            k = j
            while k<N and arr[i][k] == 1:
                    visit[i][k] = 1
                    cnt += 1
                    k+=1
            if cnt == K:
                tot += 1

# 가로, 세로 바꾸는건 행렬만 바꾸면 됨
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 막힌 곳이나 이미 방문을 한 자리이면 지나가고
            if arr[j][i] == 0 or visit[j][i] == 1: continue
            cnt = 0
            k = j
            while k < N and arr[k][i] == 1:
                visit[k][i] = 1
                cnt += 1
                k += 1
            if cnt == K:
                tot += 1
    print("#{} {}".format(tc+1,tot))