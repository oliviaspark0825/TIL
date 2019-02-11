def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("input.txt")

n, e = map(int, input().split())
n += 1 # 인덱스 쓰려고
temp = list(map(int, input().split())) # 한줄 다 받기

G = [[0 for i in range(n)] for j in range(n)]
#2차원 초기화
visited = [0 for i in range(n)] # 방문처리

for i in range(0, len(temp), 2): # 입력받으면
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
    #방향이 없어서 두번 다 해주어야 함
for i in range(n):
    print("{} {}". format(i, G[i]))


# dfs(G, 1, n)
dfs(1)

#시작점이 V 이고 돌리는 게 W  G[v][w] / w = 방문을 안했으면