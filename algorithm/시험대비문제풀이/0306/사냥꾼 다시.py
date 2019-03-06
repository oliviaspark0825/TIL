def hunt(x,y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 위, 사선오른쪽위, 오른쪽, 사선오른쪽아래, 아래, 사선 왼아래 , 왼쪽, 사선 왼위
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    # 8방향을 한 방향으로 쭉 가 보고
    for i in range(8):
        for depth in range(1, N+2):
            if forest[x + dx[i] * depth][y + dy[i] * depth] == 0 or forest[x + dx[i] * depth][y + dy[i] * depth] == 1:
                break
            elif forest[x + dx[i] * depth][y + dy[i] * depth] == 2:
                forest[x + dx[i] * depth][y + dy[i] * depth] = 9

import sys
sys.stdin = open('사냥꾼.txt')
N = int(input())
forest = [[0]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    forest[i] = [0] + list(map(int, input())) + [0]

total = 0

for i in range(N+2):
    for j in range(N+2):
        if forest[i][j] == 1:
            hunt(i,j)

for i in range(N+2):
    for j in range(N+2):
        if forest[i][j] == 9:
            total+=1

print(total)





