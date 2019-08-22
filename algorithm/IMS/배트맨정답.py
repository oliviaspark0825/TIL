import sys
sys.stdin = open('배트맨.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    # point = buildings[0]
    for h in range(len(buildings)-1):
        if buildings[h] <= buildings[h+1]: # 다음 건물 높이가 더 높으면 점프
            # point = buildings[h+1]
            cnt += 1

        else: # 작으면 건너뛰어야 함
            if h != N-2:
                cnt -= 1

    print(cnt)
