'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

import sys
sys.stdin = open("8.특별한정렬.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    max = 0
    min = 0

    for i in range(N): # 10번만 하고 버리겠다 하려면 10 을 넣어도 가능
        if i % 2 == 0: # index가 짝수이면 max 수를 넣으세요
            max = i                  # 선택정렬로 제일 작은 수 뽑아내기
            for k in range(i + 1, len(a)):
                if a[max] < a[k]:
                    max = k
            a[i], a[max] = a[max], a[i]
        else: # index가 홀수이면 min 넣기
            min = i
            for s in range(i+1, len(a)):  # 선택정렬로 제일 작은 수 뽑아내기
                    if a[min] > a[s]:
                        min = s
            a[i], a[min] = a[min], a[i]

    # new_a = a[0:10] # 10개만 뽑으라고 했으니까 슬라이싱하고
    # new_a= ' '.join(map(str, new_a)) # 리스트를 스트링으로 전환해야 출력값이 저렇게 문자열 띄어쓰기 상태로 나옴
    #
    #
    #
    # print("#{} {}".format(tc, new_a))
    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(a[i], end=" ")
    print()