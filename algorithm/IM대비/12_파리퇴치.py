import sys
sys.stdin = open('파리퇴치.txt')
T = int(input())
for tc in range(T):
    N,M = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    L = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            tot = 0
            for a in range(M):
                for b in range(M):
                    tot += arr[i+a][j+b]
            L.append(tot)

    L.sort()

    print("#{} {}".format(tc+1,L[-1]))