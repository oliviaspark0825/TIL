
import sys
sys.stdin = open("2.회문.txt", "r")

T = int(input())
for tc in range(T):


    N, M = map(int, input().split())
    print(N, M)
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(input())
    print(data)