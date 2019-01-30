import sys
sys.stdin = open("flatteningInput.txt", "r")

T = 10
for test_case in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))

    for s in range(N): # 평탄화 횟수
        max_value = 0
        max_index = 0
        min_value = 987654321
        min_index = 0

        for i in range(len(data)):   # 최댓값 최솟값

            if data[i] > max_value:
                max_value = data[i]
                max_index = i

            if data[i] < min_value:
                min_value = data[i]
                min_index = i
        data[max_index] -= 1  # 데이터 블록 수에서 하나 빼기
        data[min_index] += 1  # 데이터 블록 수에서 하나 더하기

    max_value = 0
    max_index = 0
    min_value = 987654321
    min_index = 0
    for i in range(len(data)):  # 최댓값 최솟값

        if data[i] > max_value:
            max_value = data[i]
            max_index = i

        if data[i] < min_value:
            min_value = data[i]
            min_index = i

    print('#{} {}'.format( test_case, max_value - min_value))

