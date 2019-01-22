'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''
def printlist(arr):
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end=" ")
        print()
    print()
import sys
sys.stdin = open("5.색칠하기.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):

        a1, b1, a2, b2, color = list(map(int, input().split()))

        for j in range (a1, a2 +1):
            for k in range(b1, b2 + 1):
                arr[j][k] += color
                if arr[j][k] == 3:
                    count += 1
    # printlist(arr)

    # 세기
    # for i in range(10):
    #     for j in range(10):
    #         if arr[i][j] == 3:
    #             count += 1
    print("#{} {}".format(tc, count))






