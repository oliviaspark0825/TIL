# 직사각형 종이 붙이기
import sys
sys.stdin = open("종이붙이기.txt")
T = int(input())

for tc in range(T):
    N = int(input())
    data = [1, 3]
    for x in range(2, int(N/10)):
        data.append(data[x-1] + 2*data[x-2])
    # print(data)
    print(f"#{tc+1} {data[-1]}")

