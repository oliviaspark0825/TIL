import sys
sys.stdin = open('no1.txt')
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    fruit = [list(map(int,input().split())) for _ in range(N)]
    sumlist = []
    minn = 98765

    for i in range(N-K+1):
        for j in range(N-K+1):
            sum_right = 0
            sum_left = 0
            for k in range(K):
                sum_right += fruit[i+k][j+k]
                sum_left +=fruit[i+k][K+j-k-1]
                if sum_right > sum_left:
                    sumlist.append(sum_right - sum_left)
                else:
                    sumlist.append(sum_left - sum_right)

    for a in sumlist:
        if a < minn:
            minn = a

    print(minn)

