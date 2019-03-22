T = int(input())
for tc in range(T):
    N = int(input())
    array = list(map(int, input().split()))

    start = 0
    end = len(array)
    while start < end - 1:
        max = 0
        for i in range(start + 1, end):
            if array[i] > max:
                max = array[i]
                maxidx = i
        for i in range(start, maxidx):
            array[i] = max - array[i];
        start = maxidx
    result = sum(a for a in array if a > 0)
    print(f"#{tc+1} {result-array[-1]}")