import sys
sys.stdin = open('최소신장트리.txt')
T = int(input())


def findset(x):
    if x == p[x]: return x
    else: return findset(p[x])

def mst():
    global V
    c = 0 # 간선갯수
    s = 0 # 가중치 합
    i = 0 # 제어변수
    while c < V : # V 개 -1
        p1 = findset(edge[i][0])
        p2 = findset(edge[i][1])
        if p1 != p2:
            s += edge[i][2]
            c += 1
            p[p2] = p1 # union 하는 과정
        i += 1
    return s




    # visited[u] = 1
    # total += adj[PI[u]][u]
    # for v in range(V+1):
    #     if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
    #         D[v]= adj

for tc in range(1, T+1):
    V,E = list(map(int,input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 만들때 V-1 개 만들기 0부터 시작안하니까 1개 더 만들어야함
    edge = [list(map(int,input().split())) for _ in range(E)]
    edge.sort(key=lambda x: x[2]) # 가중치 작은거부터 큰거대로
    p = list(range(V+1)) # 대표원소 초기화 == MAKE SET
    print("#{} {}".format(tc, mst()))


