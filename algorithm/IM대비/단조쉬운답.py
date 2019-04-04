import sys
sys.stdin = open('단조증가.txt')



def danjo(x):
    t = x % 10
    x = x // 10
    while x:
        if x % 10 > t:
            return False
        t = x % 10
        x = x // 10
    return True

T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    # print(A)

    max_danjo = -1
    for i in range(N):
        for j in range(i, N):
            if i != j:
                a = A[i] * A[j]
                if danjo(a):
                    if max_danjo <= a:
                        max_danjo = a

    print("#{} {}".format(tc+1, max_danjo))