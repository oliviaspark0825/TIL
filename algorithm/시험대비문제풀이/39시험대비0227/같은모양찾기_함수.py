def check(i,j):
    global M,P
    for k in range(P):  # 패턴 체크
        for l in range(P):
            if paper[i + k][j + l] != pattern[k][l]:
                return 0 # 실패하면 break 대신에 0을 보내
        #이중 끝나면 패턴 찾음 - 한번도 모양이 다른 적이 없음
    return 1

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
        if check(i,j) == 1:
            sol +=1


print(sol)