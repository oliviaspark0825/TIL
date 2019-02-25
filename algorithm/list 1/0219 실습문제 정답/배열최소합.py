def process_solution(a, k, cursum):
    global ans
    if ans > cursum : ans = cursum

def make_candidates(a, k, input, c):
    global N
    in_perm = [False] * (N+1)
# false 대신 0 , 앞에서 사용했는지 안했는지 체크
    for i in range(1, k):
        #0-1다음에 2 자리 채울 타이밍 용헸암8ㄴ
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input, cursum):
    global ans, N
#가지치기 - 현재 정답보다 크면 값이 들어갈 필요가 없으니까 제거
    if ans < cursum : return
    c = [0] * (N+1)
#candidate
    if k == input:
        process_solution(a, k, cursum) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input, cursum + data[k-1][a[k]-1])

import sys
sys.stdin = open('배열최소합_input.txt', 'r')
T = int(input())
for tc in range(T):
    ans = 987654321
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    a = [0] * (N+1)
    backtrack(a, 0, N, 0)
    #마지마 = ans 값
    print(f"#{tc+1} {ans}")