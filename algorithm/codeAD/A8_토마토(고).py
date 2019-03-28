import sys
sys.stdin = open('토마토.txt')

def tomato():
    zero = 0 # 0의 갯수
    que = []
    dx = (1,-1,0,0)
    dy = (-0,0,-1, 1)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: # 익은 토마토자리를 모두 시작점으로 큐에 저장
                que.append((i, j, 0))
            elif arr[i][j] == 0:
                zero += 1
    if zero == 0:return 0 # 모두 익힌 상태이면

 # 마킹은 굳이 필요 없음
    while que :
        x,y, day = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if arr[nx][ny] == 0: # 안익은 토마토라면
                que.append((nx, ny, day+1))
                arr[nx][ny] = 1 # 방문표시
                zero -= 1


    if zero: return -1 # zero 갯수 있으면 실패
    else:
        return day


'''
모두익힌상태?  0 가 하나라도 있으면 익힌 상태가 아님 미리 카운트하고 차감해
'''
'''
모두 익지 못하는 상황? 어딘가에 0이 있으면 못익혔네
'''
M,N = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]
# 시작좌표 찾기

print(tomato())