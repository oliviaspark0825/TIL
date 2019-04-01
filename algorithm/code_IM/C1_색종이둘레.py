import sys
sys.stdin = open('색종이둘레.txt')
N = int(input())
#0인거 확인하려면 범위가 100 넘어가니까 좀더 길게 주기
arr = [[0 for _ in range(104)] for _ in range(104)]
for n in range(N):
    cnt = 0
    r,c = list(map(int,input().split()))
    for i in range(10):
        for j in range(10):
            arr[r+i][c+j] = 1

    # 일단 1로 다 채워놓고
    for a in range(104):
        for b in range(104):
            if arr[a][b] == 1: # 일단 색칠된 자리이고
                if arr[a-1][b] == 0:
                    cnt += 1
                if arr[a+1][b] == 0:
                    cnt +=1
                if arr[a][b+1] == 0:
                    cnt +=1
                if arr[a][b-1] == 0:
                    cnt += 1
    print(cnt)
