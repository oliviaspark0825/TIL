#순차탐색 - 방향의 순서가 주어졌으니까
def iswall(x,y):
    if x<0 or x >=N: return True
    if y<0 or y >=N: return True
    if maze[x][y] == 1: return True
    return False

import sys
sys.stdin = open('미로탈출.txt')
N = int(input())
maze = [list(map(int,input())) for _ in range(N)]

direction = list(map(int,input().split())) # 1 아래, 2 왼쪽 3 위 4 오른쪽 - 다시 로테이션 시켜야 함
# indicated = {1:[1,0], 2:[0,-1], 3:[-1,0], 4:[0,1]} # 방향의 인덱스 번호를 알고 있어야 함
#이동하는 거리를 count 해주기
dr = [0, 1, 0, -1, 0]
dc = [0, 0, -1, 0, 1]
cnt = 0
r,c = 0,0 # 현재좌표
check = 9
d_no = 0 # 방향순서
while True: # 길이면 가고 장애물이면 틀어인데 횟수 제한이 없으니까
    # 한칸씩 계속이동해야하니까 현재 좌표를 들고다녀야 함
    r = r + dr[direction[d_no]]
    c = c + dc[direction[d_no]]

    if iswall(r,c) != False:
    # 벽이나 장애물이면 방향을 바꾸기
        r -= dr[direction[d_no]]
        c -= dc[direction[d_no]]
        d_no = (d_no+1)%4
    elif maze[r][c] == 0:
        maze[r][c] = check # 방문체크하고
        cnt += 1
    else:
        break


print(cnt)

# 현재좌표 vs 다음좌표를 두개를 쥐고 있으면서 갈거면 -> 갱신하기

# r = r+dr[indicated[direction[]]]
# no = 방향순서 인덱스
# dr[direction[no]]
# r = r- dr[indicated[direction[]]] # 왔던길을 되돌아가는 방법



