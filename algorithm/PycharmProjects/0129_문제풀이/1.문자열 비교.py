'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
'''
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