#두번째 그릇부터 판단을 시작해야함
# 10 + 5 +
arr = input()
tot = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        tot += 5
    else:
        tot += 10
print(tot)
