# 2*2 행렬의 합을 구한 것을 저장하고 최댓값 리턴하는 함수
def get_sum(i,j):
    global M
    sum = 0
    for x in range(M):
        for y in range(M):
            sum += data[i + x][j + y]
    return sum


import sys
sys.stdin = open('파리잡기.txt', 'r')
T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    data = [list(map(int,input().split())) for _ in range(N)]
    max = 0
    min = 987654
 # X가 열이고 Y 가 행임
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = get_sum(i,j)
            if max < sum:
                max = sum

    print("#%d %d" % (tc+1, max))
