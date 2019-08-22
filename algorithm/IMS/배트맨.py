import sys
sys.stdin = open('배트맨.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for h in range(1, N):
        if buildings[h] >= buildings[h-1]: # 다음 건물이 이전 건물보다 높을 경우, 같아도 적용되어야함
            cnt += 1

    print(cnt)