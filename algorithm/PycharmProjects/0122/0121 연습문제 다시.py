import sys
sys.stdin = open("input_100.txt", "r")


for t in range(10):
    N = int(input())  # 일단 1번 돌릴거니까
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
        sum = []  # 각 줄 합이 들어있는 리스트


    for x in range(len(arr)):  # 한 행씩 각 방의 합을 구하기
        line_sum = 0 # 한 줄 합

        for y in range(len(arr[0])):
            line_sum += arr[x][y]
        sum.append(line_sum)



    for y in range(len(arr)):  # 한 열씩 각 방의 합을 구하기
        line_sum = 0 # 한 줄 합

        for x in range(len(arr[0])):
            line_sum += arr[x][y]
        sum.append(line_sum)


    for x in range(len(arr)): # 대각선 인덱스 값이 같은 경우
        line_sum = 0  # 한 줄 합
        for y in range(len(arr[0])):
            if x == y:
                line_sum += arr[x][y]
            sum.append(line_sum)

            if x + y == len(arr)-1:
                line_sum += arr[x][y]
            sum.append(line_sum)

    sum.sort()
    print("#{} {}".format(N, sum[-1]))