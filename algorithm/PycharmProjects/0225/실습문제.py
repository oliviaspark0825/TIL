# for 문을 두개 돌려서 먼저 숫자가 0이 아닌 애를 찾았어 -> 그럼 그 시작점을 기억하고 함수로 들어가기
# 1 0이 아닌 숫자를 찾는 for 문
# 그 시작점을 기점으로 해서 행으로 쭉 돌게 하는 함수 find(

def find(x,y): # 행렬 시작좌표
        cnt = 0
        i = 0
        #돌리는 횟수가 정해지지 않았을 때에는 while 쓰기
        # x 에다가 i를 더하는 거로
        while arr[x+i][y] != 0:
                arr[x+i][j] = 0
                i += 1
        x_len = i-x
        j = 0
        while arr[x+i][y+j] != 0:
                arr[x+i][y+j] = 0
                j += 1
                cnt += 1
        y_len = j-y



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




    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0:
                find(x,y)
            else: # 다시 출발하는 시작점이 0 이면 열 길이 구하기


    print(f'#{tc+1} {cnt}')

