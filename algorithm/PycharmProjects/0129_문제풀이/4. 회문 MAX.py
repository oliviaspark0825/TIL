
import sys
sys.stdin = open("회문max.txt", "r")


def row(N, M):
    for M in range(100,0, -1):
        for x in range(N):  # 가로 각 줄에서
            for y in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[x][y + k] != arr[x][y + M - 1 - k]:
                        flag = 0
                        break # BREAK는 하나만 빠져나가기 때문에 (반복문) , 아니면 함수를 써야 한다.
                if flag == 1:
                    return M

def col(N, M):
    for M in range(100, 0, -1):
        for x in range(N):  # 세로 각 줄에서
            for y in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[y + k][x] != arr[y + M - 1 - k][x]:
                        flag = 0
                        break
                if flag == 1:
                    return M


for tc in range(10):
    T = input()
    N = 100
    M = 100
    # 100 행렬에다가 데이터 집어넣기
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(input())



    print(f'#{tc + 1} {max(row(N,M), col(N,M))}')
