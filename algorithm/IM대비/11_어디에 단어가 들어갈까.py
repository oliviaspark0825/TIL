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
            if arr[i][j] == 0 or visit[i][j] == 1: continue
            cnt = 0
            # j = k
            while visit[i][j] == 1:
                if arr[i][j] == 1:
                    cnt += 1
        if cnt == K:
            tot += 1
    print(tot)
