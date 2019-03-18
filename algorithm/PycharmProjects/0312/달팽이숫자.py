import sys
sys.stdin = open('달팽이.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr =[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = i+1