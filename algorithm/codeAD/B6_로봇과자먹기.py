def DFS(no, happ):
    global minn
    if happ>minn: return #가지치기
    if no >= N:
        # for i in range(N): print(rec[i], end=' ')
        # print(happ)
        if happ < minn: minn = happ
        return
    for i in range(N): # 과자(열번호)
        if chk[i]: continue
        chk[i] = 1
        rec[no] = arr[no] # 로봇이 행번호고 과자가 열번호니까 거리를 기록하겠다
        DFS(no+1, happ+arr[no][i]) # n 행 i 열에 있는 값을
        chk[i] = 0






import sys
sys.stdin = open('로봇.txt')
# 과자별로 체크
# 거리별로 합
T = int(input())
for tc in range(1):
    N = int(input())
    snack = list(map(int,input().split()))
    robot = list(map(int,input().split()))
    arr = [[0]*N for _ in range(N)]
    chk = [0] * N
    rec = [0] * N # 로봇별 먹은 과자의 거리 기록배열
    for i in range(N):
        for j in range(N):
            arr[i][j] = abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1] - snack[j*2+1])
    # for i in range(N):
    #     print(arr[i])
    minn = 9876543
    DFS(0,0)
    print(minn)
