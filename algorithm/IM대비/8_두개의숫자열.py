import sys
sys.stdin = open('숫자열.txt')
T = int(input())
for tc in range(T):
    N,M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    maxx = -98765
    if N<M:
        for i in range(M-N+1):
            multi = 0
            for j in range(N):
                multi += A[j]*B[i+j]
            if multi > maxx:
                maxx = multi
    else:
        for i in range(N-M+1):
            multi = 0
            for j in range(M):
                multi += B[j] * A[i + j]
            if multi > maxx:
                maxx = multi

    print("#{} {}".format(tc+1, maxx))