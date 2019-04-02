import sys
sys.stdin = open('마을위성.txt')
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# 상하좌우가 모두 1 이면 +1 하기

height = []
for i in range(1, N-1):

    for j in range(1, N-1):
        if arr[i][j]: # 일단 언덕이고, (0이 아니니까)
            # 주변에 한개라도 평지가 있으면
            if arr[i-1][j] == 0 or arr[i+1][j] == 0 or arr[i][j-1] == 0 or arr[i][j+1] == 0:
                arr[i][j] = 1
            if arr[i-1][j] != 0 and arr[i+1][j] != 0 and arr[i][j-1] != 0 and arr[i][j+1] != 0:
                height.append(arr[i-1][j])
                height.append(arr[i + 1][j])
                height.append(arr[i][j-1])
                height.append(arr[i][j+1])
                height.sort()
                arr[i][j] = arr[i][j] + height[0]


maxx = -98765
for a in range(N):
    for b in range(N):
        if arr[a][b] > maxx:
            maxx = arr[a][b]

print(maxx)

