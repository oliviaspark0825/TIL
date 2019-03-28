def DFS(no, sums):
    if no>N:
        if sums < minn:
            minn = sums
            print(minn)
        return
    for i in range(N):
        sums += data[i]

# 열이 중복하느냐 하지 않느냐





import sys
sys.stdin = open('최소의합.txt')
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
minn = flot('inf')
DFS(3,0)