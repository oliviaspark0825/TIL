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
sol = 0

#원본패턴
for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        #찾는거를 함수로 빼도 되긴 하지만, 걍 4중으로 풀어도 됨
        for k in range(P):
            for l in range(P):
                if paper[i+k][j+l] == pattern[k][l]: cnt += 1
        if cnt == P*P : sol += 1

#90 도 회전한 패턴
pattern90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        #0행부터 시작하니까 행을 고정시키고
        pattern90[j][P-i-1] = pattern[i][j]


for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if paper[i+k][j+l] == pattern90[k][l]: cnt += 1
        if cnt == P*P : sol += 1

#180 도 회전한 패턴
pattern180 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        #0행부터 시작하니까 행을 고정시키고
        pattern180[j][P-i-1] = pattern90[i][j]

for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if paper[i+k][j+l] == pattern180[k][l]: cnt += 1
        if cnt == P*P : sol += 1

#270 도 회전한 패턴
pattern270 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        #0행부터 시작하니까 행을 고정시키고
        pattern270[j][P-i-1] = pattern180[i][j]

for i in range(M-P+1):
    for j in range(M-P+1):
        cnt = 0
        for k in range(P):
            for l in range(P):
                if paper[i+k][j+l] == pattern270[k][l]: cnt += 1
        if cnt == P*P : sol += 1

print(sol)











#회전
'''    2-i
1 00  02
2 01  12
3 02  22  2
4 10  01
5 11  11
6 12  21  1
7 20  00
8 21  10
9 22  20  0

'''

