def ancestor(f1,f2): # 8, 13
    whole = []
    while f1 != 0:
        whole.append(tree[f1-1][3])
        f1 = whole[-1]
    whole.pop()
    if



    if tree[i][3] == f2 or tree[i][3] == f2:
        ans2 = i




def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

import sys
sys. stdin = open('조상.txt', 'r')
T = int(input())
for tc in range(1):
    V, E, f1,f2 = list(map(int,input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int,input().split()))
    for i in range(E):  # 2개씩 받아서 먼저 들어오면 left 방에 넣고, 아니면 righ
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
printTree()
ancestor(f1,f2)
