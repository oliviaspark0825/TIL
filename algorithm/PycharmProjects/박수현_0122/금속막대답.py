'''수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.

어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.'''
import sys
sys.stdin = open("금속막대.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    data = [[0 for _ in range(2)] for _ in range(N)] # 행 N 개 열 2개
    ans = [0] * 2 * N
    pos = 0 # 원하는 방향으로
    for i in range(N):
        for j in range(2):
            data[i][j] = temp[pos]
            pos += 1

    # 시작찾기
    spos = 0 # start position 3이 면 그다음 4, 2, 3 3개를 확인해보겠다
    while(spos < N):
        j = 0
        while(j < N):
            if data[spos][0] == data[j][1]: # 0,0 이니까 3
                break # 3, 3 같으면 빠져나가서 아래의 if로 이동
            j += 1
            if j == N: break
            spos += 1

    #ans list에 저장하기

    pos = 0 # 초기화해서 다시 시작
    ans[pos] = data[spos][0] # 2를 첫자리에 넣어라
    pos += 1
    ans[pos] = data[spos][1]
    while(1): # 다 채울때까지 while을 돌리고
        for i in range(N):
            if ans[pos] == data[i][0]:
                pos += 1
                ans[pos] = data[i][0]
                pos += 1
                ans[pos] = data[i][1]
        if pos == 2*N -1:
            break

# 출력
print("#{}".format(tc+1), end=' ')