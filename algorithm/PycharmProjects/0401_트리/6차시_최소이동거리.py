# 네비게이션 = 다익스트라



import sys
sys.stdin = open('최소이동거리.txt')
T = int(input())

def findset(x):
    if x == p[x]: return x
    else: return findset(p[x])

def dijk():
    global V
    c= 0
    s = 0 #가중치 합
    i = 0 # 제어변수
    while c != V:
        p1 = findset(edge[i][0])
        p2 = findset(edge[i][1])
        if p1 != p2:
            s += edge[i][2]
            c += 1
            p[p2] = p1  # union 하는 과정
        i += 1
    return s


for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: x[2]) # 가중치 작은거부터 큰거대로
    p = list(range(V+1))

