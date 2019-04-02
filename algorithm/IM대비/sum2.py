import sys

sys.stdin = open('s.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
row = []
col = []
tot = []
for i in range(5):
    sum1 = 0
    for j in range(5):
        sum1 += arr[i][j]
    row.append(sum1)
row.sort()
tot.append(row[-1])

for j in range(5):
    sum1 = 0
    for i in range(5):
        sum1 += arr[j][i]
    col.append(sum1)
col.sort()
tot.append(col[-1])

sum1=0
for i in range(5):
    sum1 += arr[i][i]
tot.append(sum1)

sum1= 0
for i in range(5):
    sum1 += arr[i][4-i]
tot.append(sum1)

tot.sort()

print(tot[-1])

