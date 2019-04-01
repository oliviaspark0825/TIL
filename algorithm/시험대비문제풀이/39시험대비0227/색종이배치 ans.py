import sys
sys.stdin = open('색종이배치.txt')

r1, c1, w1, h1 = map(int,input().split())
r2, c2, w2, h2 = map(int,input().split())
arr = [[0]*100 for i in range(100)] # 도화지
for i in range(r1-1, r1+h1+1): # 그려보면서 양쪽을 더 늘려주기
    for j in range(c1-1, c1+w1+1):
        if i==r1-1 or i==r1+h1 or j==c1-1 or j==c1+w1: # 가장자리이면 2로 마킹
            arr[i][j] = 2
        else:#색종이이면
            arr[i][j] = 1
# for i in range(20):
#     for j in range(20):
#         print(arr[i][j], end=" ")
#     print()


# 두번째 색종이꺼 받아오기
cnt_1 = 0
cnt_2 = 0
for i in range(r2, r2+2):
    for j in range(c2, c2+2):
        # type 1: 1: 0개, 2: 1개
        if arr[i][j] == 1:
            cnt_1 += 1
        if arr[i][j] == 2:
            cnt_2 += 1

        # type 2: 1:0개 2:2개이상
        # type 3: 1: 1개 이상
        if arr[i][j] == 1:
            print('3')
# r2, c2, w2, h2 = map(int, input().split())
# arr = [[0 for _ in range(len1)] for _ in range(len1)]
# for i in range(len1):
#     for j in range(len1):
#         arr[r1 + i][c1 + j] = 1
#
# for i in range(len1+2):
#     for j in range(len+2):
#         if arr[i][j] != 1:
#             arr[i][j] = 2

        #행과 열을 하나 뺀 좌표 // 하나 더한 좌표까지 가장자리를 2로 채우기
        #0열 0행 5열 5행을 2로 마키 i-1 j-1 00 5 5 이면은 2로 마킹, 아니면 1을 마킹해


