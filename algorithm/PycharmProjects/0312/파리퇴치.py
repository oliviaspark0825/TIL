import sys
sys.stdin = open('파리.txt')
T = int(input())
for tc in range(T):

    N,M = map(int,input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]

    max_num = -988766
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += flies[i+x][j+y]
            if total > max_num:
                max_num = total

    print('#{} {}'.format(tc+1,max_num))

