'''
for 두개로 순회를 하고, while로 1인 동안에만 체크해서 시작점을 잘못해서 중복되게 쓰지 않게
'''

import sys
sys.stdin = open('words.txt')
T = int(input())
for tc in range(T):
    N,K = list(map(int,input().split()))
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    # 가로로 찾기
    for i in range(N):
        for j in range(N):
            # 우선 visited 체크가 안된 곳만 돌아야 하니까
            if puzzle[i][j] == 1 and visited[i][j] == 0:

                linesum = 0
                a=j
                # for 문은 이렇게 바꿔놔도 위 j 는 지 갈길을 감
                # 반복의 횟수가 정해지지 않을 때는 무조건 WHILE
                while a<N and puzzle[i][a] == 1:
                    '''
                    A AND B
                    FALSE 이면 바로 다음거 실행 안함
                    '''

                    visited[i][a] = 1
                    linesum += 1
                    a += 1

                if linesum == K:
                    cnt += 1

    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if puzzle[x][y] == 1 and visited[x][y] == 0:

                linesum = 0
                b = x
                while b<N and puzzle[b][y] == 1:
                    visited[b][y] = 1
                    linesum += 1
                    b += 1

                if linesum == K:
                    cnt += 1



    print('#{} {}'.format(tc+1,cnt))



'''
더 쉬운 방법
'''
#
# T = int(input())
#
# for n in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     result = 0
#
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt += 1
#             else:
#                 if cnt == K:
#                     result += 1
#                 cnt = 0
#         if cnt == K:
#             result += 1
#
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[j][i] == 1:
#                 cnt += 1
#             else:
#                 if cnt == K:
#                     result += 1
#                 cnt = 0
#         if cnt == K:
#             result += 1
#
#     print("#{0} {1}".format(n, result))