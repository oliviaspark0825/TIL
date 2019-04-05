import sys
sys.stdin = open('최소신장트리.txt')
T = int(input())


#1 부모찾기
def find(x):
    while x != link[x]: x = link[x]
    return x

#2 같은 콤보 a 부모 == b 부모
def same(a,b):
    return find(a) == find(b)


#3 부모 합쳐주기
def unite(a, b):
    a = find(a)
    b = find(b)
    if (size[a] < size[b]):
        a, b = b, a
    siza[a] += size[b]
    link[b] = a  # b의 조상을 a로 바꿔주겠다
    return




for tc in range(1, T+1):
    V,E = list(map(int,input().split()))
    adj = [[0] * (V+1) for _ in range(V+1)]
    edge = []
    for _ in range(E):
        a, b, w = map(int,input().split())
        edge.append((a, b, w))
    edge.sort(key=lambda x: x[2]) # 가중치 작은거부터 큰거대로
    link = list(range(V+1)) # 대표원소 초기화 == MAKE SET (부모리스트)
    size = [1] * (V+1)
