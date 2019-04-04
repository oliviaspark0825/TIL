import sys
sys.stdin = open('거스름돈.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0

    k = 50000
    s = 70000
    if N // 50000:
        a = N // 50000
        N = N % 50000

    if N // 10000:
        b = N // 10000
        N = N % 10000


    if N // 5000:
        c = N // 5000
        N = N % 5000

    if N // 1000:
        d = N // 1000
        N = N % 1000

    if N // 500:
        e = N // 500
        N = N % 500

    if N // 100:
        f = N // 100
        N = N % 100

    if N // 50:
        g = N // 50
        N = N % 50

    if N // 10:
        h = N // 10
        N = N % 10

    print("#{}".format(tc+1))
    print(a,b,c,d,e,f,g,h)