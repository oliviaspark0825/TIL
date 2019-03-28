
# 눈의 중복을 허용한 중복순열-------------------
def DFS1(no):
    if no>N:
        for i in range(1, N+1): print(rec[i], end= ' ')
        print()
        return
    for i in range(1,7):
        rec[no] = i
        DFS1(no+1)


# 눈의 중복을 배제한 순열
def DFS2(no):
    if no> N:
        for i in range(1, N+1): print(rec[i], end=' ')
        print()
        return
    for i in range(1,7):
        chk[i] = 1 # 눈 사용 체크
        rec[no] = i
        DFS2(no+1)
        chk[i] =0 # 눈 사용체크 해제

 # 눈의 합의 M인 경우에만 인쇄
def DFS3(no, sums):
    if no > N:
        if sums == M:
            for i in range(1, N + 1): print(rec[i], end=' ')
            print()
        return
    for i in range(1, 7):
        rec[no] = i
        # 고른 눈만 던져주어야지 갱신이 안됨 sums += 하면 갱신이 되는거니까
        # stack 이전상태의 sums 값은 유지되어야하니까
        DFS3(no + 1, sums+i)



    # main -------------
N,M = map(int,input().split())
rec = [0] * 8 # 주사위별 눈 기록배열
chk = [0] * 7 # 눈 사용여부 체크배열
# DFS1(1) # 1번주사위부터 시작
# DFS2(1)
DFS3(1,0)
