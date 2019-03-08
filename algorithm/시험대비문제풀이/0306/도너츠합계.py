'''
항상 시작점을 잘 만들어놓고 시작하는 것을 못함, 그 친구가 유동적으로 움직이려면 for 안에서 돌아야하는것
'''


def check(x,y): # 현재 위치에서 도넛모양 합계구하기
    t1 = 0
    t2=0
    t3=0
    t4=0
    for i in range(K):
        t1 += grid[x + i][y + 2]  # 끝쪽 세로
        t2 += grid[x+i][y]
    t3 += grid[x][y+1]
    t4 += grid[x+2][y+1]
    return t1+t2+t3+t4


import sys
sys.stdin = open('도너츠.txt')
N, K = list(map(int,input().split()))
grid = [list(map(int,input().split())) for _ in range(N)]

# arr = []
# for i in range(N):
#     arr.append(list(map(int,input().split())))
donut = 0
max_d = 0

#시작점을 제어 - 도넛이 3 넘어가면 삐져나가니까, 도넛 크기만큼 줄여야 함
for i in range(N-K+1):#맵의 시작행 제어
    for j in range(N-K+1): # 맵의 시작열 제어
        donut = check(i,j)
        if donut > max_d:
            max_d = donut

print(max_d)