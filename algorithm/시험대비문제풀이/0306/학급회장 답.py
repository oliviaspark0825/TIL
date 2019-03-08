import sys
sys.stdin = open('학급회장.txt')
N = int(input())
arr = [[0] * 5 for _ in range(4)]
for i in range(N):
    score = list(map(int,input().split()))
    for j in range(1,4): # 후보자 3명 # 행은 후보
        arr[j][score[j-1]] += 1 # 점수별 카운트 # 꺼낸 점수가 index 번호가 되야함 score 인덱스 번호가 1,2,3이니까
for i in range(1, 4): # 후보자별 합계
    for j in range(1, 4):
        arr[i][4] += arr[i][j]*j

# for i in range(1, 4):
#     for j in range(1,5):
#         print(arr[i][j], end=' ')
#     print()

# max = arr[1][4]
# for i in range(2,4):
#     if arr[i][4] > max:
#         max = arr[i][4]
#         print(i, max)
#         break
#     if arr[i][4] == max:
#         for x in range(1,4):
#             if arr[x][3] > arr[x-1][3]: # 3점이 더 많은 사람
#                 print(x, max)
#                 break
#             if arr[x][2] > arr[x-1][2]: # 2점이 더 많은 사람
#                 print(x, max)
#                 break
#     else:
#         print(0, max)
maxi = 1 # 인덱스 번호로 활용하자
flag = 0
for i in range(2, 4):
    if arr[maxi][4] < arr[i][4]: # 더 큰 합계를 비교 2 번이 더 크면 갈아타면 됨
        maxi = i
        flag = 1
    elif arr[maxi][4] == arr[i][4]: # 동일합계이면 3점대 부터 비교
        for j in range(3, 1, -1): # 3점대부터 하나씩 줄여나가기 j 는 열을 뜻함
            # 두 후보간 더 큰 점수의 후보 탐색
            if arr[maxi][j] == arr[i][j] : continue
            if arr[maxi][j] < arr[i][j]: # max가 후보라는 잠정결론
                maxi = i
            # 아니라면,
            flag = 1 # 후보자 찾았으니까
            break


    if flag == 1:
        break
print(maxi,arr[maxi][4])




