def perm(n,k):
    global N, route
    # 시작점을 주고 이후부터는 도착점을 시작으로 주어서 계속 돌게

    if n == N+1:
        for i in range(n):
            route.append(i)
    else:
        for i in range(n, k):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]


import sys
sys.stdin = open('전기카트.txt')
T = int(input())
for tc in range(1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    route = []
    perm(N+1,1)
    print(route)
    # 일단 route 안에 숫자를 1을 고정시킨다음에 n-1만큼 숫자를 집어넣기

