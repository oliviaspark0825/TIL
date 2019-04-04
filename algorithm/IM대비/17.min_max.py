import sys
sys.stdin = open('minmax.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    minn = float('inf')
    maxx = -9876554321
    for i in range(N):
        if data[i] > maxx:
            maxx = data[i]

        if data[i] < minn:
            minn = data[i]


    ans = maxx - minn
    print("#{} {}".format(tc+1, ans))