# import sys
# sys.stdin = open('달팽이.txt')
N= int(input()) # 모눈종이 데이터 받기
arr = [[0 for _ in range(N)] for _ in range(N)]

r,c = 0, -1 # 한칸 이전 위치에서 시작
num = 0 #카운팅할 숫자
cnt = N # 루프 회전수
while num < N*N:
    #오른쪽방향
    for i in range(cnt):
        c += 1 # 열좌표만 증가하면서 오른방향으로
        num += 1
        arr[r][c] = num
    cnt -= 1 # 회전수 하나씩 줄어가니까
    # 아래방향
    for i in range(cnt):
        r += 1 # 행좌표만 증가하면서 오른방향으로
        num += 1
        arr[r][c] = num
    # 왼쪽
    for i in range(cnt):
        c -= 1 #  열만 감소하면서 왼방향으로
        num += 1
        arr[r][c] = num
    cnt -= 1
    # 위쪽
    for i in range(cnt):
        r -= 1 # 행좌표만 감소하면서 위방향으로
        num += 1
        arr[r][c] = num

print(arr)