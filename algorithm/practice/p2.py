T = int(input())

def gogo(x, y):
    global arr, cnt

    if arr[x][y+1] == 9:
        arr[x][y+1] = cnt
        gogo(x, y+1)

    if arr[x][y-1] == 9:
        arr[x][y-1] = cnt
        gogo(x, y-1)

    if arr[x+1][y] == 9:
        arr[x+1][y] = cnt
        gogo(x+1, y)

    if arr[x-1][y] == 9:
        arr[x-1][y] = cnt
        gogo(x-1, y)

    return

for n in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    sum_max = 0
    sum_ea = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if sum_max < arr[i][j]:
                sum_max = arr[i][j]

            if arr[i][j] != 0:
                arr[i][j] = 9

    cnt = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 9:
                arr[i][j] = cnt
                gogo(i, j)
                cnt += 1

    sum_ea = cnt-1

    print('#{0} {1} {2}'.format(n, sum_ea, sum_max))