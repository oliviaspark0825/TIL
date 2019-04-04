import sys
sys.stdin = open('구간합.txt')
T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    L = []
    for i in range(N-M+1):
        sums = 0
        for j in range(M): # M번만큼 더해야하는거고, 데이터가 1차원이니까
            sums += data[i+j]
        L.append(sums)
    L.sort()
    ans = L[-1] - L[0]
    print("#{} {}".format(tc+1, ans))