def BFS(G,s):
    global n
    visited = [0]*n # 방문표시할 방 생성
    queue = []
    queue.append(s) # 시작점 v 를 큐에 삽입
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            print(t)
        for i in G[t]: # t에 인접한 모든 정점을 구하려면
            if not visited[i]:
                queue.append(i)
s = 1
G = 7
n = 8
data = list('1213242546566737')
print(BFS(7,1))

#DFS 로 할 경우


def dfs(V):
    global E, visited, adj, V, flag # G = 도착 노드,  V = 노드갯수 // 매번 쓰기위해


    visited[v] = 1 # 방문한 곳은 1로 표시하여 재방문하지 않도록
    if v == E:
        flag = 1
        return

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
    return

V = 7
E = 8
data = list('1213242546566737')
# 2차원 초기화
adj = [[0 for i in range(V+1)] for j in range(V+1)]
# 인접 노드 방문할 경우 카운트할 방 생성
visited = [0 for i in range(V+1)]

for s in range(E):
    x, y = data? # 인접한거 나열한 데이터를 받아서
    adj[x][y] = 1 # 해당하는 인접 행렬에 1을 표시
