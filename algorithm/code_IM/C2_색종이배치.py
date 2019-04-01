import sys
sys.stdin = open('색종이배치.txt')
x1, y1, w1, h1 = list(map(int,input().split()))

arr = [[0]*100 for i in range(100)]

for i in range(x1-1, x1+h1+1): # 가로 길이만큼
    for j in range(y1-1, y1+w1+1):
        # 가장자리이면 2 색칠하고
        if i == x1-1 or i == x1+h1  or j == y1-1 or j == y1+w1:
            arr[i][j] = 2
        else:
            arr[i][j] = 1

x2, y2, w2, h2 = list(map(int,input().split()))
cnt1 = 0
cnt2 = 0
for x in range(x2, x2+h2):
    for y in range(y2, y2+w2):
        if arr[x][y] == 2:
            cnt2 += 1

        elif arr[x][y] == 1:
            cnt1 += 1

if cnt1 == 0 and cnt2 == 1:
    sol = 1
elif cnt1 == 0 and cnt2 > 1:
    sol = 2
elif cnt1 > 0:
    sol = 3
else:
    sol = 4

print(sol)


# sr, sc, w, h = map(int, input().split())
# arr = [[0] * 100 for i in range(100)]
#
# for i in range(sr - 1, sr + h + 1):
#     for j in range(sc - 1, sc + w + 1):
#         if i == sr - 1 or i == sr + h or j == sc - 1 or j == sc + w:
#             arr[i][j] = 2
#         else:
#             arr[i][j] = 1
#
# sr, sc, w, h = map(int, input().split())
# cnt1 = 0
# cnt2 = 0
# for i in range(sr, sr + h):
#     for j in range(sc, sc + w):
#         if arr[i][j] == 1:
#             cnt1 += 1
#         elif arr[i][j] == 2:
#             cnt2 += 1
#
# if cnt1 == 0 and cnt2 == 1:
#     sol = 1
# elif cnt1 == 0 and cnt2 > 1:
#     sol = 2
# elif cnt1 > 0:
#     sol = 3
# else:
#     sol = 4
#
# print(sol)