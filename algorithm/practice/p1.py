T = int(input())

for n in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 99999999
    for i in range(N-K+1):
        for j in range(N-K+1):
            stack_1 = sum([arr[i + k][j + k] for k in range(K)])
            stack_2 = sum([arr[i + k][j + K - 1 - k] for k in range(K)])
            if min_num > max(stack_1, stack_2) - min(stack_1, stack_2):
                min_num = max(stack_1, stack_2) - min(stack_1, stack_2)
    print('#{0} {1}'.format(n, min_num))
