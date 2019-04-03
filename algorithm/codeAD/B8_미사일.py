'''
군함을 중복순열을 해야함
군함이 없는 바다에 던지면 소용 없다 - 이미 침몰한 자리는 필요 없음
맞은 군함을 기준으로 다 루프를 돌려서 차감해야 함
'''
def clear(no):# 현재 군함위치에서 반경이내 에너지 모두 차감
    for i in range(N):
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
    if temp <= R:
        arr[i][2] -= P
def update(no): # 현재 군함위치에서 반경이내 에너지 모두 복원
    for i in range(N):
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
    if temp <= R:
        arr[i][2] += P
def DFS(no):
    global sol
    # 현재 no 미사일을 모든 군함에 쏘아보는 경우의 수시도
    # 단, 군함이 침몰하지 않은 군함에만 시도
    if no==M:
        cnt =0 # 남아있는 군함의 갯수
        for i in range(N):
            if arr[i][2] > 0: cnt +=1
        if cnt <sol: sol = cnt
        return # depth가 끝이라면
    for i in range(N): # 군함
        if arr[i][2] <= 0: continue # 침몰한 군함은 시도 불가
        clear(i) # 현재 군함 반경이내 모든 군함에너지 차감
        DFS(no+1) # 다음 미사일로
        update(i) #  복원해ㅜ



import sys
sys.stdin = open('미사일.txt')
#########
N = int(input())
arr =[]
for i in range(N):
    arr.append(list(map(int,input().split())))
M,P,R = list(map(int,input().split()))
sol = 16
temp = 0
DFS(1) # 1번미사일부터 시작
print(sol)