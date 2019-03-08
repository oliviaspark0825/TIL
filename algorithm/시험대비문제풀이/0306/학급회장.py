import sys
sys.stdin = open('학급회장.txt')
N = int(input())
vote = [list(map(int,input().split())) for _ in range(N)]
print(vote)
candidate = {'1':0, '2':0, '3':0}
for i in range(N):
    # for j in range(3):
        candidate['1'] += vote[i][0]
        candidate['2'] += vote[i][1]
        candidate['3'] += vote[i][2]

print(candidate)

p1 = {'1':0, '2':0, '3':0}
for i in range(N):
    if vote[i][0] == 1:
        p1['1'] += 1
    if vote[i][0] == 2:
        p1['2'] += 1
    if vote[i][0] == 3:
        p1['3'] += 1
print(p1)

p2 = {'1':0, '2':0, '3':0}
for i in range(N):
    if vote[i][1] == 1:
        p2['1'] += 1
    if vote[i][1] == 2:
        p2['2'] += 1
    if vote[i][1] == 3:
        p2['3'] += 1
print(p2)

p3 = {'1':0, '2':0, '3':0}
for i in range(N):
    if vote[i][2] == 1:
        p3['1'] += 1
    if vote[i][2] == 2:
        p3['2'] += 1
    if vote[i][2] == 3:
        p3['3'] += 1
print(p3)
# 1을 맥스로 잡고 2, 3 비교

