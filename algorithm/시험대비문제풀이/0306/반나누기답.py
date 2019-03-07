def check(s, e):
    cnt=0
    cnt=sum(arr[s:e+1])
    if k_min <= cnt <= k_max:
        return cnt

import sys
sys.stdin = open('반나누기.txt')
T = int(input())
for i in range(T):
    N, k_min, k_max = [int(i) for i in input().split()]
    arr= [0]*101
    temp = list(map(int,input().split()))


    for score in temp:
        arr[score] += 1

    sol = 100
    cnt = [0]*3
    for i in range(1, 100-1): # 98까지만 가고
        for j in range(i+1,100): # B 반의 끝요소
            cnt[0] = check(1,i)
            cnt[1] = check(i+1,j)
            cnt[2] = check(j+1,100)
            if cnt[0]*cnt[1]*cnt[2]==0: continue # 하나라도 실패하면, 0이 되니까
            temp = max(cnt) - min(cnt)
            if temp < sol: sol = temp
    if sol == 100:
        print(-1)
    else:
        print(sol)