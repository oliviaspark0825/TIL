'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # n 행렬에다가 데이터 집어넣기
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(input())
    print(f'#{tc + 1}', end =' ')
    for x in range(N):  # 가로 각 줄에서
        for y in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if arr[x][y+k] != arr[x][y+M-1-k]:
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    print(arr[x][y+k], end ='')
    for x in range(N):  # 가로 각 줄에서
        for y in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[y + k][x] != arr[y + M - 1 - k][x]:
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    print(arr[y + k][x], end='')

    print()

