import sys
sys.stdin = open('기지국.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N+1)]
    # 집 == H, 기지국 A =1 B = 2 C= 3
    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'A':
                if 0 <=i-1< N+1 and  0 <=i+1< N+1 and  0 <=j-1< N+1 and  0 <=j+1< N+1:
                    arr[i+1][j] = 0
                    arr[i-1][j] = 0
                    arr[i][j-1] = 0
                    arr[i][j+1] = 0

    dx = [0,1, -1, 0]
    dy = [1, 0, 0, -1]
    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'B':
                if 0 <=i-1< N+1 and  0 <=i+1< N+1 and  0 <=j-1< N+1 and  0 <=j+1< N+1 and 0 <= i - 2 < N + 1 and 0 <= i + 2 < N + 1 and 0 <= j - 2 < N + 1 and 0 <= j + 2 < N + 1:
                    arr[i+1][j] = 0
                    arr[i-1][j] = 0
                    arr[i][j-1] = 0
                    arr[i][j+1] = 0
                    arr[i + 2][j] = 0
                    arr[i - 2][j] = 0
                    arr[i][j - 2] = 0
                    arr[i][j + 2] = 0
    # for d in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]

    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'C':
                if 0 <=i-1< N+1 and 0 <=i+1< N+1 and  0 <=j-1< N and  0 <=j+1< N:
                    arr[i+1][j] = 0
                    arr[i-1][j] = 0
                    arr[i][j-1] = 0
                    arr[i][j+1] = 0
                if 0 <= i - 2 < N + 1 and 0 <= i + 2 < N + 1 and 0 <= j - 2 < N and 0 <= j + 2 < N:
                    arr[i + 2][j] = 0
                    arr[i - 2][j] = 0
                    arr[i][j - 2] = 0
                    arr[i][j + 2] = 0
                if 0 <= i - 3 < N + 1 and 0 <= i + 3 < N + 1 and 0 <= j - 3 < N and 0 <= j + 3 < N:
                    arr[i + 3][j] = 0
                    arr[i - 3][j] = 0
                    arr[i][j - 3] = 0
                    arr[i][j + 3] = 0
    cnt = 0
    for a in range(N+1):
        for b in range(N):
            if arr[a][b] == 'H':
                cnt += 1

    print("#{} {}".format(tc+1, cnt))
