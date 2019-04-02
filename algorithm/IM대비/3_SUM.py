import sys
sys.stdin = open('sum.txt')
T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    tot = []
    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += arr[i][j]
        tot.append(sum1)

    for j in range(100):
        sum1 = 0
        for i in range(100):
            sum1 += arr[i][j]
        tot.append(sum1)

    cross_x = 0
    for i in range(100):
        cross_x += arr[i][i]
    tot.append(cross_x)
    cross_y = 0
    for i in range(100):
        cross_y += arr[-i-1][i]
    tot.append(cross_y)

    tot.sort()

    print("#{} {}".format(tc+1, tot[-1]))
