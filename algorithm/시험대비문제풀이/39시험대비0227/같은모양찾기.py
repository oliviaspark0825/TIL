import sys
sys.stdin = open('같은모양찾기.txt')
M = int(input()) # 모눈종이 데이터 받기
paper = []
for i in range(M):
    paper.append(list(map(int,input())))
P = int(input()) # 패턴 받기
pattern = []
for i in range(P):
    pattern.append(list(map(int,input())))
# 모양이 다르면 계속 체크할 필요 없음
# 패턴 9 개가 모두 같은지 count
# 모양이 다르면 - break 2번 걸어야 함

sol = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        flag = 0 # 여기서 초기화 해야, break로 패턴 한번 체크하고 빠져나갈때, 초기화되어서 다시 시작
        cnt = 0
        for k in range(P):         # 패턴 체크
            for l in range(P):
                #패턴이 같지 않을 경우
                #같이 따라가야하니까 이동을 같이 따라가야 함
                if paper[i+k][j+l] != pattern[k][l]:
                    flag = 1
                    # print(i,j)
                    break
                else: # 패턴과 같으면 카운트해주기
                    cnt += 1
            if flag == 1:
                break # flag를 체크를 해서 나가게 하자 flag
        # k, l 이중루프를 다 돈 시점
        if cnt == P*P:
            sol += 1

print(sol)

#         if check(x,y) == 1:
#             sol += 1
#
# for
#     if a[][] != b[][]