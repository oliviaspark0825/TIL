def find(v, G, D):
    stack = list()
    for i in range(1, v+1):
        if (D[i] == 0):
            stack.append(i)

    while(len(stack) !=0):
        t = stack.pop()
        print(t, end= ' ')
        for i in range(1, v + 1):
            if (G[t][i] == 1):
                D[i] -= 1
                if (D[i] == 0):
                    stack.append(i)







import sys
sys.stdin = open("경로추가.txt")
T = int(input())

for tc in range(T):
    flag = 0
    V,E = list(map(int, input().split()))

    edge = [[0 for i in range(V+1)] for j in range(V+1)]  # 2차원 초기화
    # 인접 노드 방문할 경우 카운트할 방 생성
    D = [0] * (V+1)
    # for i in range(E):
    # n1 = edge[i * 2]
    # n2 = edge[i * 2 +1]
    for s in range(E):
        n1 = edge[i]
        n2 = edge[i +1]
        G[n1][n2] = 1
        D[edge[i*2 + 1]] += 1  #     진입차수
    print('#{}'. format(tc+1), end=' ')
    find(v, G, D)

    S,G =map(int, input().split())