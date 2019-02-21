import sys
sys.stdin = open('최대수.txt', 'r')
T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    max = -10000
    for i in range(0, len(data)):
        if data[i] > max:
            max = data[i]
    print(f'#{tc+1} {max}')