
# n개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수

arr = [-7, -3, -2, 5, 8]
sum = 0
count = 0

# for i in range(1 << n):
#
#     for j in range(n):
#         sum = nums[i][j]
#         if sum == 0:
#             count += 1

for i in range(1, 1 << len(arr)): # 2 ** n 승을 의미하는 것  2 **len(Arr)
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]  # 한칸씩 1을 보내겠다

    if sum == 0:
        count += 1
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end=' ')

        print()
print("개수 : {}".format(count))

