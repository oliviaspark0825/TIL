def binaryS(x, P):
    left = 1
    right = P
    count = 0

    while left <= right:
        middle = 0
        middle = int((left + right) // 2)
        count += 1
        if x == middle:  # 검색성공하면
            return count
        elif x < middle:
            right = middle
        else:
            left = middle
import sys
sys.stdin = open("7.이진탐색.txt", "r")
T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    a = int(binaryS(Pa, P))
    b = int(binaryS(Pb, P))

    if a>b:
        winner = 'B'
    elif a == b:
        winner = '0'
    else:
        winner = 'A'

    print("#{} {}".format(tc, winner))