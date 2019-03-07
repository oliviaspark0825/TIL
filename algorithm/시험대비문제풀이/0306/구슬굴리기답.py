import sys
sys.stdin = open('구슬굴리기.txt')
N,N = list(map(int,input().split()))
map = [[1]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    maze[i] = [1] + list(map(int, input())) + [1]
way = int(input())
direction = [int(i) for i in input().split()]
