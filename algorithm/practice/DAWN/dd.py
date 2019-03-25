def solve(x): # 123
    t = x % 10 #3
    x //= 10 #12
    while x:
        if x % 10 > t:
            return False
        t = x % 10
        x //= 10

    return True

import sys
sys.stdin = open('단조증가.txt')
T= int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    rst = -1
    for i in range(N-1):
        # 항상 j가 커야하니까
        for j in range(i+1,N):
            num = data[i] * data[j]
            if solve(num):
                if rst < num:
                    rst = num

    print('#{} {}'.format(tc + 1, rst))