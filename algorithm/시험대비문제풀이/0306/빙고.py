def find(number):
    global arr
    for i in range(5):
        for j in range(5):
            if arr[i][j] == number:
                arr[i][j] = 0
                return

def bingo():
    ans = 0
    Xsum1, Xsum2 = 0, 0
    for i in range(5):
        Rsum, Csum,  = 0, 0
        for j in range(5):
            Rsum += arr[i][j]
            Csum += arr[j][i]  # 세로 합이 동시에 구해짐 n * n 전제하에
        if Rsum == 0: ans +=1 # 가로 세로 합이 나왔을 때 0이면 ans + 1
        if Csum == 0: ans +=1
        Xsum1 += arr[i][i]
        Xsum2 += arr[i][N - i - 1]

    if Xsum1 == 0: ans +=1
    if Xsum2 == 0:ans +=1
    if ans >= 3:return True
    else:return False

import sys
sys.stdin = open('빙고.txt')
# arr = []
# for i in range(5):
#     arr.append(list(map(int,input().split())))
arr = [list(map(int,input().split())) for _ in range(5)]
answer = [list(map(int,input().split())) for _ in range(5)]
N = 5
# 한줄이 비워졌다 - 모두 더했을 때 0 이면 끝 / 가로, 세로 대각선
# 합을 더해서 0인게 3개 이상이면 빙고로 멈추기
# 사회자가 숫자 부르면 그 숫자 가지고 이중루프 돌기 1
#2 빙고인지 아닌지 판단하는 함수 - 가로세로 양방향 대각선 합 0 이 몇개인지
flag = 0
for i in range(N):
    for j in range(N):
        find(answer[i][j]) #해당 숫자를 찾아 지우기
        if bingo() == True: # 빙고 3줄 찾으면 탈출
            flag =1
            break
    if flag == 1: break
# for i in range(5):
#     print(*arr[i])


print(i*5 + j + 1) #사회자가 부른 횟수
# 행이 늘어나는건 열의 갯수만큼 곱해주기