import sys
sys.stdin = open('no1.txt')
T = int(input())
for tc in range(T):
    N, K = list(map(int,input().split()))
    fruit = [list(map(int,input().split())) for _ in range(N)]

    substract = []
    minn = 987654

    for i in range(N-K+1):
        for j in range(N-K+1):
            cross_left = 0
            cross_right = 0
            for s in range(K):
                    cross_right += fruit[i+s][j+s]
                    cross_left += fruit[i+s][K+j-1-s]
                    if cross_right > cross_left:
                        substract.append(cross_right-cross_left)
                    else:
                        substract.append(cross_left-cross_right)


    for i in substract:
        if i < minn:
            minn = i

    print(minn)

