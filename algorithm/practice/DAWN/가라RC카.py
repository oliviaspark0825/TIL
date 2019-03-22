import sys
sys.stdin = open('words.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    for n in range(N):
        idx, velo = list(map(int,input().split()))
        start_v = 0
        if idx == 1: # 가속이면



