def perm(n,r,q):
    if r == 0:

    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            perm(n-1, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]




import sys
sys.stdin = open('배열.txt')
T = int(input())
L = []
for tc in range(T):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    a = list(range(1,N+1))
    t = [0] * N
    min_num = 999999999999

print(N,N,N)