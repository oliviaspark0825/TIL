# 정렬 검색
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:  # 해당 값이 없으면 다음 idx 로 넘어가야하니까 증가시켜주기
        i = i + 1

    if i < n:
        return i  # idx 는 전체보다 -1 길이 짧아야하니까
    else:
        return -1  # n 과 크기가 같으면 잘못된거니까

    for i in range(n):
        if a[i] == key:
            return i
        else:
            return -1


data = [4, 9, 11, 23, 2, 19, 7]
key = 20
print(sequentialSearch(data, len(data), key))