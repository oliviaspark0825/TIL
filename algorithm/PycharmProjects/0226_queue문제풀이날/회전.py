import sys
sys.stdin = open('회전.txt', 'r')
T = int(input())
for tc in range(T):
    N, M = list(map(int,input().split()))
    data = list(map(int,input().split()))
    # stack = []
    L = []
    # #M번동안 계속 스택에 쌓는다
    # for i in range(M):
    #     for s in range(N):
    #         stack.append(data.pop(0))
    # print(stack)
    #
    #
    for i in range(N):
        n = M % N
        L = data[n]
    print(f'#{tc+1} {L}')