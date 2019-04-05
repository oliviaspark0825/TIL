import sys
sys.stdin = open('최대높이섬.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
