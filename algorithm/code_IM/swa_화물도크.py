
import sys
sys.stdin = open('화물도크.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    t = [list(map(int,input().split())) for _ in range(N)]
    t.sort(key=lambda x: x[1])
    # 종료와 동시에 새로운 도크 가능함
    cnt = 0
    end = 0

    for i in range(N):
        if end<=t[i][0]:
            cnt += 1
            end = t[i][1]
    print('#{} {}'.format(tc,cnt))

