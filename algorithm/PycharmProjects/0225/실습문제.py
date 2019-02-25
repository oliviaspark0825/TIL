import sys
sys.stdin = open('실습문제.txt', 'r')
T = int(input())
for tc in range(1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(5):
        arr[i] = list(map(int,input().split()))
    print(arr)
    #행렬의 행과 열의 길이
    x_len = 0
    y_len = 0


# for 문을 두개 돌려서 먼저 숫자가 0이 아닌 애를 찾았어 -> 그럼 그 시작점을 기억하고 함수로 들어가기
# 1 0이 아닌 숫자를 찾는 for 문
# 그 시작점을 기점으로 해서 행으로 쭉 돌게 하는 함수 find(

def find(x,y): # 행렬 시작좌표
        cnt = 0
        i = 0
        while arr[x+i][y] != 0:
                arr[x+i][j] = 0
                i += 1
        j = 0
        while arr[x+i][y+j] != 0:
                arr[x+i][y+j] = 0
                j += 1
                cnt += 1



for x in range(N):
    for y in range(N):
        if arr[x][y] != 0:
            find(x,y)
        else: # 다시 출발하는 시작점이 0 이면 열 길이 구하기
            y_len =

    print(f'#{tc+1} {cnt}  ')




    # for x in range(N):
    #     for y in range(N):
    #         if arr[x][y] != 0:
    #             x += 1
    #             arr[x][y] = 0
    #         # 0을 만나면 행의 길이를 바로 전 x 값으로 구하고 아래로 내려가면서 열의 길이 구하기
    #         else:
    #             x_len = x-1
    #             y += 1
    #             if arr[x][y] != 0:
    #                 y += 1
    #                 arr[x][y] = 0
    #             else:
    #                 y_len = y-1
    #
    #
    #
    #
