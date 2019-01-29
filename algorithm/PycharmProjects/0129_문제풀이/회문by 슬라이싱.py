'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
'''

import sys
sys.stdin = open("2.회문.txt", "r")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # n 행렬에다가 데이터 집어넣기
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(input())


        # 가로

    for x in range(N): # 가로 각 줄에서
        for y in range(N-M+1):
            new_arr = arr[x][y:y+M]  # M 길이의 새로운 정렬
            if new_arr == new_arr[::-1]:
                ans = new_arr
                print(ans)

    #  #세로
    empty = []
    for j in range(M):
        for k in range(N-M+1):
            empty = arr[k][j]
            if empty == empty[::-1]:
                ans = empty
                print(empty);

    # print(f'#{tc+1} {}')