import sys
sys.stdin = open('백만장자.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    money = 0
    max = 0

    for i in range(n - 1, -1, -1):  # 뒤에서 부터 큰값을 찾아서
        if max > data[i]:
            money += max - data[i]
        else:
            max = data[i]
    print("#{} {}".format(tc + 1, money))