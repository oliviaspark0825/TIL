import sys
sys.stdin = open('단조증가.txt')


def check(x):
    global L
    namoji = x % 10
    mok = x // 10
    while mok // 0 != 0:
        z.append(x // 10)
        x = x % 10
        if x // 10 == 0:
            z.append(x)



T = int(input())
for tc in range(1):
    N = int(input())
    data = list(map(int, input().split()))
    L = []
    new = []
    # 우선 서로 곱한 값 만들기
    for i in range(N-1):
        for j in range(i+1,N):
            one = data[i]*data[j]
            # if check(one):

