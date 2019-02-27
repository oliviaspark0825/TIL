import sys
sys.stdin = open('색종이초.txt')
N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    r,c = map(int,input().split())
    cnt = 0
    # 색종이 범위만큼 1을 더해주기
    for i in range(10):
        for j in range(10):
            arr[r+i][c+j] = 1
# 일단 1로 채우는걸 다 끝낸 후에 갯수를 카운트하는게 낫겠지? for 문 나오기
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)

    # for i in range(3, 3+10): # (10)으로 주고
    #     for j in range(7, 7+10):
    #         arr[i][j] = 1 # arr[3+i][7+i] 로 적어서 시작을 하면 되겠지?
            # 1면적을 싹 더하면 면적이겠지?