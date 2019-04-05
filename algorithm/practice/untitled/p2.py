import sys, time
sys.stdin = open('p2.txt')

st = time.time()

def find(N,M):
    def combination_sum(sect):
        maxN = 0
        for i in range(6):
            for j in range(i+1, 6):
                for k in range(j+1, 6):
                    # result = [i,j,k]
                    maxN = max(maxN, abs(sect[i]-sect[j]) + abs(sect[j]-sect[k]) + abs(sect[k]-sect[i]))
        return maxN

    def section(garo, sero1, sero2):
        nonlocal N, M
        sect = [0 for _ in range(6)]
        for i in range(N):
            for j in range(M):
                if i <= garo:
                    if j <= sero1:
                        sect[0] += matrix[i][j]
                    elif sero1 < j <= sero2:
                        sect[1] += matrix[i][j]
                    else:
                        sect[2] += matrix[i][j]
                else:
                    if j <= sero1:
                        sect[3] += matrix[i][j]
                    elif sero1 < j <= sero2:
                        sect[4] += matrix[i][j]
                    else:
                        sect[5] += matrix[i][j]
        return combination_sum(sect)

    result = []
    for garo in range(N-1):
        for sero1 in range(M-2):
            for sero2 in range(sero1+1,M-1):
                result += [section(garo, sero1, sero2)]
    return max(result)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(tc), find(N,M))
print(time.time()-st)