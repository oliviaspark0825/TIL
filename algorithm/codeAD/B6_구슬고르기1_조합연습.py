#조
#합 순서 상관없이 골랐다 안골랐다, 있기만 하면 됨


a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
    if no >= N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
    # O 담기
    b[no] = a[no]
    DFS(no+1)
    #X 안 담기
    b[no] = 0
    DFS(no+1)

def DFS2(no, cnt): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
    # if cnt == 2:
    #     for i in range(N): print(b[i], end=' ')
    #     print("cnt:{}".format(cnt))
    #     return

    if no >= N:
        for i in range(N): print(b[i], end=' ')
        print(cnt)
        return
    # O 담기
    # b[no] = a[no]
    b[cnt] = a[no] # 순서대로 하고싶으면
    DFS2(no+1, cnt+1)
    #X 안 담기
    b[no] = 0
    DFS2(no+1, cnt)


# 1] 리턴조건 : N번째이면 인쇄후 리턴
# 2] 현재 구슬을 고르기(b배열에 담기)
# 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)

# main ============================
# DFS(0) # a[0]요소 구슬부터 시작
DFS2(0,0)