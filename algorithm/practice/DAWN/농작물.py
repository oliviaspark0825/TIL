# 중간을 찾아서 시작을 줄이고 끝을 늘리고,

import sys
sys.stdin = open('농작물.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    total = 0
    mid = N//2
    start,end = mid, mid
    for i in range(N):
        # y 좌표 값을 시작점은 -1 하고 끝점을 +1 하려면 그 가운데 y 좌표를 두개로 놓고 하나는 -1 다른거 하나늠 +1 로
        for j in range(start,end+1,1):
            total += data[i][j] # 해당 행에서 다 더하고 j 좌표가 달라져야 하니까
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print('#{} {}'.format(tc+1,total))




