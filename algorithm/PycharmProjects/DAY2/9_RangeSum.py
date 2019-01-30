# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


import sys

sys.stdin = open("9input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 정수 갯수 와 이웃할 M 갯수 받기
    a = list(map(int, input().split()))  # 정수 받아오기

    max = 0
    min = 987654321
    ans = 0
# 1,2,3 더하기 해야하는데 1~10이면 8까지 해야하는데 8의 INDEX == 7
    # for가 두번 들어가니까 n**
    # min / max 잘 구하는 것이 문제
    for i in range(N-M+1): # N 개의 정수 중에서 1~7 까지이면 i 는 1,2,3,4,5 까지이니까
        sum = 0 # 다 더한다음에 SUM 을 0으로 셋팅하고 새로 시작
        for j in range(M): # s를 기준으로 더해야하는 정수 갯수 범위 내에서
            sum += a[i+j]
        if sum > max: max = sum
        if sum < min: min = sum
    ans = max - min


    print('#{} {}'.format(test_case, ans))


