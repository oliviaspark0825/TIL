def bfs(v):
    global G, V

    queue = []
    queue.append(v) # 시작점 v 를 큐에 삽입
    visited[v] = 1
    print(v, end=' ')
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1): # t에 인접한 모든 정점을 구하려면
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                # 방문을 계속 더해주면 거리를 구할 수 있음
                print(w, end=' ')



import sys
sys.stdin = open('연습문제3.txt', 'r')
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):
    print("{} {}".format(i, G[i]))

bfs(1)

