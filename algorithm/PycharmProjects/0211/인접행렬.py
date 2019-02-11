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

# DFS_Recursive(G, v)
#   visited[v] True
#
# for each all w in adjacency(G, v)
#      if visited[w] != True
#     dfs_recursive(G,v)

def dfs(G, y, n):
 for i in range(G)

dfs(G, 1, n)
