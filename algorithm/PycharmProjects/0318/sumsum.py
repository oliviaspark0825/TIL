import sys
sys.stdin = open('sum.txt')
for tc in range(10):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    L = []

    for i in range(100):
        rows = 0
        for j in range(100):
            rows += arr[i][j]
        L.append(rows)

    for i in range(100):
        cols = 0
        for j in range(100):
            cols += arr[j][i]
        L.append(cols)

    cross_right = 0
    for i in range(100):
        cross_right += arr[i][i]
    L.append(cross_right)

    cross_left = 0
    for i in range(100):
        cross_left += arr[-i-1][i]
    L.append(cross_left)


    print(max(L))
    print(min(L))