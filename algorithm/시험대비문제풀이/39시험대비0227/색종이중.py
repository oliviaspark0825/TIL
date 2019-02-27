import sys
sys.stdin = open('색종이중.txt')
N = int(input())
# 배열은 좀 넓게 주기
arr = [[0 for _ in range(102)] for _ in range(102)]
# arr = [[0]*100 for i in range(100)]
for k in range(N):
    r,c = map(int,input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1 # 색종이 붙이기

# 이 안에 0과 1 밖에 없고, 상관관계가 있을까
#0과 1이 서로 맞닿아 있는 부분만 둘레인거임
# 1을 찾아서 - 시작점으로 하고, 4방향을 다 확인하고, 방문처리해야하는듯?
#상하좌우에서 0의 갯수 = 둘레
# 0의 위치에서 하면 map을 벗어나니까
tot = 0
for i in range(102):
    for j in range(102):
        if arr[i][j] == 1:
            if arr[i-1][j] == 0: # 상
                tot += 1
            if arr[i+1][j] == 0: # 하
                tot += 1
            if arr[i][j-1] == 0: # 좌
                tot += 1
            if arr[i][j+1] == 0: # 우
                tot += 1
print(tot)

