import sys
sys.stdin = open('색칠하기.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))

    mat = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0

    for z in range(N):
        if arr[z][4] == 1:
            for a in range(arr[z][0], arr[z][2]+1):
                for b in range(arr[z][1], arr[z][3]+1):
                    if mat[a][b] == 2:
                        mat[a][b] = 3
                    else:
                        mat[a][b] = 1

        if arr[z][4] == 2:
            for a in range(arr[z][0], arr[z][2]+1):
                for b in range(arr[z][1], arr[z][3]+1):
                    if mat[a][b] == 1:
                        mat[a][b] = 3
                    else:
                        mat[a][b] = 2

    for x in range(10):
        for y in range(10):
            if mat[x][y] == 3:
                cnt +=1

    print("#{} {}".format(tc+1, cnt))





#import sys
#sys.stdin = open("5.색칠하기.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):

        a1, b1, a2, b2, color = list(map(int, input().split()))

        for j in range (a1, a2 +1):
            for k in range(b1, b2 + 1):
                arr[j][k] += color
                # if arr[j][k] == 3:
                #     count += 1
    # printlist(arr)

    # 세기
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
    print("#{} {}".format(tc, count))