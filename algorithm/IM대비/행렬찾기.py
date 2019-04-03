def find(x,y):
    a, b = 0, 0
    while arr[x+a][y] : a += 1
    while arr[x][y+b] : b += 1
    # i = 0
    # while arr[x + i][y]:
    #     j = 0
    #     while arr[x + i][y + j]:
    #         arr[x + i][y + j] = 0
    #         j += 1
    #     i += 1

    for i in range(a):
        for j in range(b):
                arr[x+i][y+j] = 0

    return (a,b)

# 왜 아래에서 튜플하면 안되는지?



import sys
sys.stdin = open('행렬찾기.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    matlist = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                matlist.append(find(i,j))
                cnt += 1

    matlist.sort(key=lambda x:(x[0]*[1], x[0]))
    matlist.sort(reverse=True)
    ans = []
    for z in range(len(matlist)):
        ans.append(matlist[z][0])
        ans.append(matlist[z][1])

    print("#{} {}".format(tc+1, cnt), end=" ")
    print(*ans)
