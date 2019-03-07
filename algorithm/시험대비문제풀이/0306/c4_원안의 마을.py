import sys, math
sys.stdin = open('원안의마을.txt')
N = int(input())
map = [list(map(int,input())) for _ in range(N)]
max = 0
village = []
# 기지국 위치 좌표부터 찾기
for i in range(N):
    for j in range(N):
        if map[i][j] == 2:
            x,y = i,j
        elif map[i][j] == 1:
            village.append([i,j])

for v in village:
    [a,b] = v
    d = ((x-a)**2 + (y-b)**2)**0.5
    if d > max:
        max = d
print(math.ceil(max))

