import sys
sys.stdin = open('최소의합.txt')


def DFS1(no, nsum): # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum>nmin : return # 가지치기: 합이 nmin 초과시 리턴
    # 뎁스 결정은 행 수니까, 행보다 많아지면 나가라
    if no>= N:
        # 어떤 구슬 값을 골랐는지 확인하기 위해 프린트 찍고, 합도 찍고
        for i in range(N): print(rec[i], end= ' ')
        print(':{}'.format(nsum))
        if nsum < nmin: nmin = nsum
        return
    # depth 끝나면 최솟값비교해랑
    for i in range(N): #열
        rec[no] = arr[no][i]# 주사위 번호를 인덱스로 썼으니까, 그리고 고른 값을 기록하자
        # 무조건 다음 뎁스지 옛날에 for j in range 하는 그거! 그걸 재귀로하겠다고
        DFS1(no+1, nsum + arr[no][i]) # 행은 no 이고, 열은 i 니까

# 중복을 허요하지 않겠다, 그냥 순열
def DFS2(no, nsum):
    global nmin
    # if nsum > nmin: return  # 가지치기: 합이 nmin 초과시 리턴
    # 뎁스 결정은 행 수니까, 행보다 많아지면 나가라
    if no >= N:
        # 어떤 구슬 값을 골랐는지 확인하기 위해 프린트 찍고, 합도 찍고
        for i in range(N): print(rec[i], end=' ')
        print(':{}'.format(nsum))
        if nsum < nmin: nmin = nsum
        return
    # depth 끝나면 최솟값비교해랑
    for i in range(N):  # 열
        if chk[i]: continue
        chk[i] = 1
        rec[no] = arr[no][i]  # 주사위 번호를 인덱스로 썼으니까, 그리고 고른 값을 기록하자
        # 무조건 다음 뎁스지 옛날에 for j in range 하는 그거! 그걸 재귀로하겠다고
        DFS2(no + 1, nsum + arr[no][i])  # 행은 no 이고, 열은 i 니까
        chk[i] = 0






N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
rec = [0] * N # 고른 값을 기록배열(debugging)
chk = [0] * N # 열 체크 배열
nmin = float('inf')
# DFS1(0,0)
DFS2(0,0)
print(nmin)