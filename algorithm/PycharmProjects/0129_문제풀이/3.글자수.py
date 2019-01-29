'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

'''
import sys
sys.stdin = open("3.글자수.txt", "r")
T = int(input())
for tc in range(T):
    N = list(map(str,input()))
    M = list(map(str,input()))
    alpha = dict()

    # N 문자열로 딕셔너리 생성
    for i in range(len(N)):
        alpha.update({N[i]: 0 })

    #N 과 M을 비교해서 같은 문자가 있을 경우 딕셔너리 value 값 count하기
        for y in range(len(M)):
            if N[i] == M[y]:
                alpha[N[i]] += 1
    # value 값들에서 max 값 찾기
    max = 0
    for v in alpha.values():
        if v > max:
            max = v

    print(f'#{tc + 1} {max}')




