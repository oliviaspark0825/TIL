
# 프린트 출력함수 만들기
def printArr():
    for i in range(N+1):
        for j in range(N):
            print(arr[i][j], end="")
        print()
    print()


    printArr()

import sys
sys.stdin = open('기지국.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N+1)]
    # arr = [list(input() for _ in range(N)]
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
    for x in range(N+1):
        for y in range(N):
            if arr[x][y] == 'B':
                for d in range(4):
                    for s in range(1,3):
                        nx = x + s*dx[d]
                        ny = y + s*dy[d]
                        if nx<0 or nx>=N+1 or ny<0 or ny>=N: continue
                        else:
                            arr[nx][ny] = 0


    for x in range(N + 1):
        for y in range(N):
            if arr[x][y] == 'C':
                for d in range(4):
                    for l in range(1,4):
                        nx = x + l * dx[d]
                        ny = y + l * dy[d]
                        if nx < 0 or nx >= N + 1 or ny < 0 or ny >= N: continue
                        else:
                            arr[nx][ny] = 0
    cnt = 0
    for a in range(N+1):
        for b in range(N):
            if arr[a][b] == 'H':
                cnt += 1

    print("#{} {}".format(tc+1, cnt))

    #
    #
    #
    # for k in range(1, ord(map[i][j]) - ord('A')+2):
    #     if i + k < N and arr[i+k][j] == 'H':
    #         arr[i+k][j] = 'X'
    #     if j + k < N and arr[i + k][j+k] == 'H':
    #         arr[j + k][i] = 'X'