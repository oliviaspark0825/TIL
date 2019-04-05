# makeset, findset , union

def findset(x):
    if x == p[x]: return x
    else: return findset(p[x]) # 찾을때까지 재귀

def union(a,b):

    p[findset(b)] = findset(a)


import sys
sys.stdin = open('그룹나누기.txt')
T = int(input())
for tc in range(T):
    N,M = list(map(int,input().split()))
    data = list(map(int,input().split()))
    p = list(range(N+1)) # 부모 리스트 만들기

    for i in range(0,len(data),2):
        union(data[i],data[i+1])
    # p의 값을 다 부모로 바꾸고 싶으면
    # for i in range(1,N+1):
    #     p[i] = findset[i]
    # ps = set()
    # for i in range(1, N+1):
    #     ps.add(findset(i))
    count = 0
    for i in range(1, N+1):
        if i == p[i]: count +=1;


    print("#{} {}".format(tc+1,count))