'''
도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다. '''
# 최대 정류장 수 = K

import sys
sys.stdin = open("7input.txt", "r")

T = int(input()) # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int,input().split))
    idx = 0 # 현재 버스 위치
    for idx in range(N):
        while idx + K < N:
            idx = idx + K
            if idx == bus_stop:
                True
            if idx != bus_stop









# print('#{} {}'.format(test_case, ans))
