import sys
sys.stdin = open('치킨.txt')

def solve(): # 열을 돌려야 함 그래서 ji

    sums = 0
    for i in range(HN): # 기준은 집 현재 집에서 고른 치킨집과 최소인 거리 찾기
        dist_min = 20*20
        for j in range(CN): #치킨집
            if not sel[j]: continue # 선택안한 치킨집이면 스킵
            dist_min = min(dist_min,arr[j][i]) # 최소거리
        sums += dist_min
    return sums

def DFS(no,cnt):
    global sol
    # M개 골랐을 때 고른 치킨과의 최소 거리 합 비교
    if cnt == M:
        # for i in range(CN): print(sel[i], end=' ')
        # print()
        sums = solve()
        if sums < sol: sol=sums
        return
    if no>= CN:
        return

    # 현재 치킨집을 고르거나 고르지 않는 경우 시도
    sel[no] = 1 # 3개중에 두개 고르기
    DFS(no+1, cnt+1)
    sel[no] = 0
    DFS(no+1, cnt)


#main----------------
N,M = list(map(int,input().split()))
temp = []
for i in range(N):
    temp.append(list(map(int,input().split())))
house = []
chk = []

# 치킨집과 집 정보 정리하기
for i in range(N):
    for j in range(N):
        if temp[i][j] == 2: # 치킨집
            chk.append((i,j))
        elif temp[i][j] == 1:# 집
            house.append((i,j))

CN = len(chk) # 치킨집갯수
HN = len(house) # 집 갯수
arr= [[0]*HN for _ in range(CN)]
for i in range(CN): # 행을 치킨집
    for j in range(HN):
        # 치킨집과 집 거리 계산
        dist = abs(chk[i][0] - house[j][0]) + abs(chk[i][1] - house[j][1])
        arr[i][j] = dist

sel = [0] * HN # 고른 치킨집
rec = [0] * CN
sol = 20 * 20

DFS(0,0) # 0행 (첫번째

print(sol)