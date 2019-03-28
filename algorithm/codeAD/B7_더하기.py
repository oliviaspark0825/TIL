def DFS(no, tot):
    global flag

    if flag or tot > K: return
    if tot == K:
        flag = 1
        return
    if no >= N:
        # for i in range(N): print(box[i], end=' ')
        # print(tot)
        # if tot == K:
        #     flag = 1
        return

    chk[no] = 1
    box[no] = arr[no]
    DFS(no+1, tot + arr[no])

    chk[no] = 0
    box[no] = 0
    DFS(no + 1, tot)




import sys
sys.stdin = open("더하기.txt")
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    chk = [0] * N
    box = [0] * N
    flag = 0
    DFS(0,0)

    if flag == 1:
        print('YES')
    else:
        print('NO')

