import sys
sys.stdin = open('전구.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    data = [0] +list(map(int, input().split()))
    led = [0] * (N+1)
    cnt = 0
    for i in range(1,N+1):
        if data[i] != led[i]:
            cnt+=1
            for j in range(i,N+1,i):
                if led[j] == 1:
                    led[j] = 0
                else:
                    led[j] = 1

    print(cnt)