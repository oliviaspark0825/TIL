def DFS(no, tot):
    global N, K, flag

    if no >= N:
        if tot == K:
            return 1
        # return 0
        # for i in range(N):print(box[i], end=' ')
        # print(tot)
        # return
        return
    chk[no] = 1
    box[no] = arr[no]
    DFS(no+1, k+1, tot + arr[no])

    chk[no] = 0
    box[no] = 0
    DFS(no + 1, k+1, tot)




import sys
sys.stdin = open("더하기.txt")
T = int(input())
for tc in range(1):
    N,K = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    chk = [0] * (N+1)
    box = [0] * (N+1)
    flag = 0
    DFS(0,0)

    if flag == 1:
        print('YES')
    else:
        print('NO')