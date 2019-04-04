import sys
sys.stdin = open("행렬찾기.txt")

# 행렬의 시작부터 크기를 세면서 0으로 바꾸기
def findarr(x, y):
    r, c = 0, 0
    while L[x+r][y]: r += 1
    while L[x][y+c]: c += 1

    for i in range(r):
        for j in range(c):
            L[x+i][y+j] = 0

    return r, c

T = int(input())
for tc in range(T):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    # print(L)

    A = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if L[i][j]:
                A.append(findarr(i, j))
                cnt += 1
    print(A)
    A.sort(key=lambda x: (x[0]*x[1], x[0]))    # 정렬 기준 요소 순서대로 써주기
    print(A)
    ans = []
    for i in range(len(A)):
        ans.append(A[i][0])
        ans.append(A[i][1])
    # print("#{} {}".format(tc + 1, cnt), *ans)