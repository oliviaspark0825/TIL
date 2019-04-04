# 첫번째에 사용한 재료를 기억해놓고. 고른 갯수
# 잔상을 지워야지 그다음거를 담을 수 있음
# 함수 하나당, 내가 지금 어떤거를 시도했느지 하나만 들고다니기 -그럼 기록 지울필요도 없음
# 재료별로 갯수 카운팅
def DFS(start, cnt):
    global sol
    if cnt == M:
        # for i in range(cnt): print(rec[i], end= ' ')
        # print()
        sol += 1
        return
    for i in range(start, N): # 흙의재료
        if rec[cnt] == arr[i]: continue # 같은 자리에 같은 재료 안담게
        rec[cnt] = arr[i]
        DFS(i+1, cnt+1) # 담았으니까 하나 더 늘이고
    rec[cnt] = 0 # 지워줘야함 갔다 돌아오면 무조건 지우는게 아님 / 모든 경우의 수 시도가 끝나면
    # 11 12 13 13 또 3 담으면 같으니까 되돌아가기
import sys
sys.stdin = open('도자기.txt')
T = int(input())
for tc in range(T):
    N,M = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    rec = [0]*N
    cnt = [0] * N
    sol = 0
    DFS(0,0)
    print(sol)