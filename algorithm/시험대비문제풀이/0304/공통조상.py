def ancestor(f1,f2):
    whole = []
    while f1 != 0:
        whole.append(tree[f1][2])
        f1 = whole[-1]
    begin = tree[f2][2]
    while begin:
        if begin in whole:
            return begin
        begin = tree[begin][2]

def preorder(V):
    global cnt
    if V != 0:
        cnt += 1
        preorder(tree[V][0])
        preorder(tree[V][1])


def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

import sys
sys. stdin = open('조상.txt', 'r')
T = int(input())
for tc in range(T):
    V, E, f1,f2 = list(map(int,input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int,input().split()))
    cnt = 0
    for i in range(E):  # 2개씩 받아서 먼저 들어오면 left 방에 넣고, 아니면 righ
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1
    same_root = ancestor(f1,f2)
    preorder(same_root)
    print("#{} {} {}".format(tc+1, same_root, cnt))
