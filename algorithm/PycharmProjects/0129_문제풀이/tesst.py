import sys
sys.stdin = open("1.문자열비교.txt", "r")

def is_same(N, M):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    check_list = []
    while j < len(N) and i < len(M):
        if M[i] != N[j]:
            i = i - j
            j = -1
        i = i + 1 # 다음 인덱스 확인해야하니까 하나씩 증가
        j = j + 1
    if j == len(N):
        return 1 # 검색 성공
    else:
        return 0 # 검색 실패


T = int(input())
for tc in range(T):
    N = list(map(str,input()))
    M = list(map(str,input()))
    result = is_same(N,M)




    print("#{} {}".format((tc+1),result))