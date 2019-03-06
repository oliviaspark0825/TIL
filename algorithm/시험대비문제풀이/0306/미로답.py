import sys
sys.stdin = open('미로탈출.txt')
N = int(input())
maze = [[1]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    maze[i] = [1] + list(map(int, input())) + [1]
direction = list(map(int,input().split())) # 1 아래, 2 왼쪽 3 위 4 오른쪽 - 다시 로테이션 시켜야 함
# indicated = {1:[1,0], 2:[0,-1], 3:[-1,0], 4:[0,1]} # 방향의 인덱스 번호를 알고 있어야 함
#이동하는 거리를 count 해주기
dr = [0, 1, 0, -1, 0]
dc = [0, 0, -1, 0, 1]
cnt = 0
r,c = 1,1 # 현재좌표
check = 9
d_no = 0 # 방향순서
while True: # 길이면 가고 장애물이면 틀어인데 횟수 제한이 없으니까
    # 한칸씩 계속이동해야하니까 현재 좌표를 들고다녀야 함
    r = r + dr[direction[d_no]] # 1번 방에 가서 증감치를 꺼내와라
    c = c + dc[direction[d_no]]

    if maze[r][c] == 0:
        maze[r][c] = check # 방문체크하고
        cnt += 1
    elif maze[r][c] == 1:
        # 진행방향에서 역으로 갈 거니까
        r -= dr[direction[d_no]]
        c -= dc[direction[d_no]]
        d_no += 1
        if d_no == 4:
            d_no = 0
    else:
        break

print(cnt)