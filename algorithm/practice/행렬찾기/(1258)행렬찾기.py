#우선 0이 아닌 숫자를 찾는 for 2 개로 돌리고


#선택정렬 - 가장 작은 애를 찾아서 바꾸기
def selectionSort(arr, cnt): # cnt 는 행렬 갯수, 지금은 3개
    for i in range(cnt - 1):
        min = i
        for j in range(i+1, cnt):
            x = arr[min][0] * arr[min][1]
            y = arr[j][0] * arr[j][1]
            if x > y:
                min = j
            elif x == y and arr[min][0] > arr[j][0]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def get_submatrix(x, y):
    global submatrix, subcnt
    #행 단위로 돌아야하니까
    #while 바로 위에 초기화, 나올때 - 증가시키기
    i = 0
    # x+ i = 행
    while data[x+i][y]: # 0 이 아니면 참이니까
        j = 0
        while data[x+i][y+j]:
            data[x+i][y+j] = 0 # 0으로 값을 바꿔주기
            j += 1
        i += 1 # i 더해주면 증가하니까 행이 한줄 아래로
    submatrix[subcnt][0] = i
    submatrix[subcnt][1] = j
    subcnt += 1


import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)] #한줄로 받기
    submatrix = [[0 for _ in range(2)] for _ in range(20)] #부분행렬 최대 20개

    subcnt = 0 # 행렬 갯수 세기 위한 카운트
    for i in range(N):
        for j in range(N):
            if data[i][j]: # 0 이 아니면은 이렇게 쓰쟈
                get_submatrix(i, j)

    selectionSort(submatrix, subcnt)

    print(f"#{tc+1} {subcnt}", end=" ")
    for i in range(subcnt):
        print(f"{submatrix[i][0]} {submatrix[i][1]}", end=" ")
    print()
