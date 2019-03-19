N,K = list(map(int,input().split()))
donut= [list(map(int,input().split())) for _ in range(N)]
minn = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        tot = 0
        for m in range(i, i+K):
            for n in range(j, j+K):
                if (m == i or m == i+k) or if(n==i or n==j+k):
                    tot += donut[m][n]
                    if tot < minn:
                        minn = tot
print(minn)
