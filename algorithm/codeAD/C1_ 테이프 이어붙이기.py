'''
n 개 중에 n-1 구하기
count 들고다니기
'''

import sys
sys.stdin = open('테이프.txt')
def DFS(no,cnt,sums):
    global sol
    if cnt + (N-no) < N/2: return # 남아있는게 절반보다 적으면 굳이 들어갈 필요 없으니까
    if cnt == N//2:
        temp = abs(sums - (tot-sums)) # 이등분한 테이프의 차이
        if temp<sol: sol=temp
    return # n의 위치에 갔을 때까지

    if no>=N:
        # 합 찍어보기
        # for i in range(N): print(rec[i], end=' ')
        #print(cnt, sums)
        return
    # 현재 no번 테이프를 붙이거나 붙이지 않는 경우의 시도
    rec[cnt] = arr[cnt] # 내가 방금 고른거를 기록하기
    DFS(no+1, cnt+1, sums + arr[no])
    rec[cnt] = 0  # 안골랐으면 기록 지우고
    DFS(no + 1,cnt, sums)
    # n/2개를 고른 경우만 길이의 차 비교


N = int(input())
arr = list(map(int,input().split()))
rec = [0] * N
sol = 500*20
tot = sum(arr)
DFS(0,0,0) # 0번째 테이프부터 시작, 고른개수 0개, 테이프길이 합
print(sol)