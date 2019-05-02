dr = [ -1, -1, -1] # 이건 다 위로만 가면 되는거고
dc = [-1, 0, 1] # 위왼, 위, 위오 니까
def check(r,c):
    # 현재 좌표에 퀸을 놓을 수 있는지 여부 체크
    for i in range(3): # 3방향
        for k in range(1,N): # 1배, 2배, 증감치의 배수 계산
            nr = r + dr[i]*k
            nc = c + dc[i]*k
            if nr< 0 or nr >=N or nc<0 or nc >=N: break
            if arr[nr][nc] == 1: return 0 # 놓을 수 없음 실패
    return 1 # 놓을 수 있음 성공

def DFS(no):
    global sol
    # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    if no >= N: # 한판 완성
        sol += 1
        return
    #  도달하지 않았으면
    for i in range(N): # 열
        if chk1[i]: continue # 세로방향체크
        if chk2[no + i]: continue # 오른쪽대각선방향 체크 # 행과 열
        if chk3[(N-1)-(no-i)]: continue # 왼쪽대작선
        chk1[i]= chk2[no + i] = chk3[(N-1)-(no-i)] =1
        DFS(no + 1)
        chk1[i] = chk2[no + i] = chk3[(N - 1) - (no - i)] = 0




'''
행마다 0,1,2,3 열중에 어디에 넣어야할지 고르고
겹치는지 확인해야함
'''
N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 = [0] * N
chk2 = [0] *(N*2)
chk3 = [0] *(N*2)

sol = 0
DFS(0) # 0행부터 시작
print(sol)