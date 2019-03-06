import sys
sys.stdin = open('구슬굴리기.txt')
N,N = list(map(int,input().split()))
map = [list(map(int,input())) for _ in range(N)]
way = int(input())
direction = [int(i) for i in input().split()]
print(direction)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dno = 0
r, c = 1, 1
check = 9
cnt = 0
while True:
    r = r + dr[direction[dno]]
    c = c + dc[direction[dno]]
    if map[r][c] == 0:
        map[r][c] = check
        cnt += 1

    elif map[r][c] == 1



