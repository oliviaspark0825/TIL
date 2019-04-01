import sys
sys.stdin = open('색종이초.txt')
N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    r, c  = list(map(int,input().split()))
    cnt = 0
    # 정사각형이니까
    for i in range(10):
        for j in range(10):
        # 정사각형 길이만큼 1을 채우라
        # 당연히 배열이니까 for 두개지
            arr[r+i][c+j] = 1
    for a in range(100):
        for b in range(100):
            if arr[a][b] == 1:
                cnt +=1
print(cnt)