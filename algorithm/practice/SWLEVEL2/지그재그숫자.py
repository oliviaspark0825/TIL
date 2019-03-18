import sys
sys.stdin = open('지그재그.txt')
T= int(input())
for tc in range(T):
    N = int(input())
    total = 0
    numbers = []
    for i in range(1,N+1):
        numbers.append(i)

    for n in numbers:
        if n % 2:
            total += n
        else:
            total -= n

    print('#{} {}'.format(tc+1,total))
