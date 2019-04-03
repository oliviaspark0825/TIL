a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
chk = [0, 0, 0] # 구슬 사용여부 체크
N = 3

# no 는 b 배열의 index! 0번부터 시작했으니까 3 이면 탈출
# 1개 뭘 담을 까 2개째에 뭘 담을까 고민하는 것
def DFS(no): #현재 no번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우
    #1] 리턴조건 : 3개를 고른후 인쇄한 후 리턴
    if no>=N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    #2] a배열에서 0요소부터 N전요소전까지 고르는 모든 경우(단 구슬중복 배제)
    for i in range(N): # a[i] a 배열에 있는 구슬을
        if chk[i] : continue# 체크되어있으면 skip
        chk[i] = 1 # 안되어있으면 사용하겠다
        b[no] = a[i]
        DFS(no +1) # 이제 2개 째 뭘 담을까
        chk[i] = 0 # 체크 해제
        b[no] = 0 # 어차피 덮어쓸거라서


# main ============================
#
# import sys
# sys.stdin = open('구슬고르기.txt')
DFS(0) # b[0]요소부터 담기 시작

