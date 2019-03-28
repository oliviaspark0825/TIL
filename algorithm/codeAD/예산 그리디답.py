
# greedy method

import sys
sys.stdin = open('예산.txt')
#
# def check(m):
#     # 상한액으로 지방에서 요청액을 배정가능하면 - 배정, 아니면 상한액으로 합계 계산
#     tot = 0
#     for i in range(N):
#         if arr[i] <= m:
#             tot += arr[i]
#         else:
#             tot += m
#         # 합계가 총핵 이하이면 성공 아니면 실패 리턴
#     if tot <= M: return 1
#     else: return 0


#main  ------------------------------
N = int(input())
arr = list(map(int,input().split()))
M = int(input())
arr.sort()
sol, tot = 0, 0
for i in range(N):
    if tot + arr[i]*(N-i) <= M: #  현재 예산액으로 배정 가능하면 총액 이하면
        tot += arr[i]
    else:    # 현재 예산액으로 배정 불가능하면
        sol =(M - tot) //(N-i)
print(sol)