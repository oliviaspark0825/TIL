import sys
sys.stdin = open('magnetic.txt')
T =10
for tc in range(1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    tot_cnt = 0


    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt = 1
            if arr[j][i] == 2:
                if cnt == 1:
                    tot_cnt += 1
                cnt = 0


    print("#{} {}".format(tc+1, tot_cnt))