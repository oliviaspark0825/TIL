def DFS(no, sums):
    global minn
    if sums>minn:
        return #가지치기
    if no >= N:
        if sums < minn:
            minn = sums
        return
    for i in range(N): # 과자(열번호)
        if chk[i]: continue
        chk[i] = 1
        rec[no] = building[no] # 로봇이 행번호고 과자가 열번호니까 거리를 기록하겠다
        DFS(no+1, sums+building[no][i]) # n 행 i 열에 있는 값을
        chk[i] = 0



import sys
sys.stdin = open('건물세우기.txt')
N = int(input())
building =[list(map(int,input().split())) for _ in range(N)]
chk = [0] * N
rec = [0] * N
minn = float('inf')
DFS(0,0)
print(minn)