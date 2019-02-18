# 그래프경로

def dfs(v):
    global G, visited, adj, V, flag # G = 도착 노드,  V = 노드갯수 // 매번 쓰기위해



    visited[v] = 1 # 방문한 곳은 1로 표시하여 재방문하지 않도록
    if v == G:
        flag = 1
        return

    #재귀는 들어가자마자  visited =1 하고 시작
    # if s == goal :
    #     flag = 1
    #     return
    # visited[s] = 1

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
    return


import sys
sys.stdin = open("그래프경로.txt")
T = int(input())

for tc in range(T):
    flag = 0
    V,E = list(map(int, input().split()))

    adj = [[0 for i in range(V+1)] for j in range(V+1)]  # 2차원 초기화
    # 인접 노드 방문할 경우 카운트할 방 생성
    visited = [0 for i in range(V+1)]

    for s in range(E):
        x, y = map(int, input().split())
        adj[x][y] = 1

    S,G =map(int, input().split())

    dfs(S)
    print(f'#{tc+1} {flag}')
    # flag 대신에 visited[G]













