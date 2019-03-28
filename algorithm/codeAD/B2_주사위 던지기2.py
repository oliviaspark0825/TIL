'''
for을 n번 돌릴 수 없으니까 ---> 재귀로 풀어야지
중복순열
'''
   #no= 주사위 번호
def DFS(no):
    if no >N:
        # 합 구하려면
        if sum == M:
            print(for 돌려서 찍기)
            return
    # else 안써도 됨 어차피 리턴 못당하면 내려오니까
    # 1번 2번 주사위라는거지
    # 무조건 1~6까지 배열에 돌리자
    for i in range(1,7): # 눈의 역할
        # 인덱스를 뎁스로 들어가는 주사위 번호
        rec[no] = i
        # 이 다음에 for인데 이거 대신에 재귀하자
        DFS(no+1)


    # 중복
    for i in range(1,7):
        if chk[i]: continue # 체크되어있으면 pass
        chk[i] = 1 # 아니면 눈 사용
        rec[no] = i
        DFS(no+1)
        chk[i] = 0 # check 했던거 다시 해제
 # 여기서 다시 해제 안하면 중복순열인거고, 다시 풀고 또 하면 중복조합인거고



# 합이 m 인거 확인하기








import sys
sys.stdin = open('주사위.txt')



for i in range(1,7):
    for j in range(1,7):
        put(i,j)



