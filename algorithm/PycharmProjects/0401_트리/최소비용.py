import sys
sys.stdin = open('최소비용.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(intkinput().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(N):
        for y in range(N):
            
