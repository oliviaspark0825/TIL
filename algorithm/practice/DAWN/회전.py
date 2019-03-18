import sys
sys.stdin = open('숫자회전.txt')
T = int(input())
for tc in range(1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    turn_90 = [[0]*n for _ in range(n)]
    turn_180 = [[0]*n for _ in range(n)]
    turn_270 = [[0]*n for _ in range(n)]
    ans = []

# # 원래 배열의 1열이 90도 회전된 배열에선 1 행이니까
    for i in range(n):
        for j in range(n):
                turn_90[i][j] = arr[n-j-1][i]

    for i in range(n):
        for j in range(n):
                turn_180[i][j] = turn_90[n-j-1][i]

    for i in range(n):
        for j in range(n):
                turn_270[i][j] = turn_180[n-j-1][i]
    for array in zip(turn_90, turn_180, turn_270):
        for top in array:
            print(*top, end=" ")
        print()