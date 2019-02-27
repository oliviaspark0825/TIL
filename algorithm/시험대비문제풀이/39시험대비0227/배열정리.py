#2차원 배열 돌리기
import sys
sys.stdin = open('배열정리.txt', 'r')
X,Y = list(map(int,input().split()))
data = [list(map(int,input().split()))for _ in  range(X)]

#연속으로 1을 찾으면 OR 이전꺼가 1
for i in range(len(data)):
    cnt = 1
    for j in range(len(data[i])-1):
        if data[i][j] != 0 and data[i][j+1] == 1:
            cnt += 1
            data[i][j+1] = cnt
        elif data[i][j] != 0 and data[i][j+1] == 0:
            cnt = 1


for a in range(len(data)):
    for b in range(len(data[a])):
        print(data[a][b], end= ' ')
    print()

#
'''
R, C = map(int, input())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split()))
for i in range(R):
    for j in range(1, C):
        iff arr[i][j] == 1:
        arr[i][j] += arr[i][j-1]
for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')
    print()
'''