def binaryS(x, P):
    left = 0
    right = P
    middle = 1
    count = 0

    while left <= right:
        middle = int((left + right) // 2)
        if x == middle:  # 검색성공하면
            count += 1
            return count

        elif x < middle:
            right = middle - 1
            count += 1
        else:
            left = middle + 1
            count += 1

print(binaryS(23, 300))