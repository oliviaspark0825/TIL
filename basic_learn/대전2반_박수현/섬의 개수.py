def island(x,y):
    cnt = 0
    dno = 0
    # 좌, 우, 아래
    dr = [0, 0, 0, 1]
    dc = [0,-1, 1, 0]
    #시작 좌표
    r, c = x, y
    max_height = 0
    while True:
        r += dr[dno]
        c += dc[dno]
        # 벽이면 다시 돌아라
        if r < 0 or r >= N: continue
        if c < 0 or c >= N: continue
        # 0이면 다시 이전 좌표로 돌아가서 돌아야 하고
        if map[r][c] == 0:
            r -= dr[dno]
            c -= dc[dno]
            dno += 1
            if dno == 3:
                dno = 0
        # 섬이면 - 높이가 max_height 보다 크면 저장, 0으로 바꿔서 방문처리
        elif map[r][c] != 0:
            if map[r][c] > max_height:
                max_height = map[r][c]
            map[r][c] = 0

    cnt += 1
    return cnt


# import sys
# sys.stdin = open('섬의 개수.txt')
T= int(input())
for tc in range(T):
    N = int(input())
    map = [list(map(int,input().split())) for _ in range(N)]
# print(map)
# 섬의 갯수
total = 0

for i in range(N):
    for j in range(N):
        if map[i][j] != 0:
            total += island(i,j)


#
# # 최대 섬 높이
# max_height = 0
# for i in range(N):
#     for j in range(N):
#             if map[i][j] >= max_height:
#                 max_height = map[i][j]

print("#{} {} {}".format(tc+1,total, max_height))

