# def iswall(x, y):
#     if x < 0 or x >= N: return True
#     if y < 0 or y >= N: return True
#
#     return False
#
def check(x,y,sums):
    global N, minn
    # 계속 좌표를 보내줌으로써 n-1 갈때까지 돌 함수
    sums += data[x][y]
    if x == N-1 and y == N-1:
        if sums < minn:
            minn = sums
        return
    if y+1 <N:
        check(x,y+1,sums)
    if x+1 <N:
        check(x+1,y,sums)

#
# def check(x,y):
#     global minn
#     total = data[0][0]
#     dx = [0, 1]
#     dy = [1, 0]
#     while idx !=2:
#         nx = x + dx[idx]
#         ny = y + dy[idx]
#         if iswall(nx,ny) == False:
#             total += data[nx][ny]
#             if idx == 1:
#                 idx = 0
#
#
#         if nx == N-1 and ny == N-1:
#             if total < minn:
#                 minn = total
#                 return minn
#         idx += 1


import sys
sys.stdin = open('최소합.txt')
T= int(input())
for tc in range(T):
    N = int(input())
    # for i in range(N):
    #     data = list(map(int,input().split()))
    data = [list(map(int,input().split())) for _ in range(N)]
    minn = float('inf')

    check(0,0,0)

    print("#{} {}".format(tc+1, minn))