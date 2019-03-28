import sys, time
from time import strftime
start_time = time.time()
def perm(n,k,sums):
    global minn
    if n ==k:
        sums = 0
        for i in range(N-1):
            # 각 houses 간의 거리를 구해서 더해준다
            sums += (abs(houses[i][0]-houses[i+1][0]) + abs(houses[i][1]-houses[i+1][1]))
            # 최솟값을 구해야하니까
        if sums < minn:
            minn = sums

    else:
        for i in range(k, n):
            # 시작데이터부터 끝까지 계산한 것
            total_sum = (abs(data_all[k-1][0] - data_all[k][0]) + abs(data_all[k-1][1]-data_all[k][1]))
            data_all[i], data_all[k] = data_all[k], data_all[i]
            perm(n, k+1, sums+total_sum)
            data_all[i], data_all[k] = data_all[k], data_all[i]



sys.stdin = open("최적경로.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))  # 회사, 집, N 명 고객 좌표
    company =[data.pop(0), data.pop(0)]
    home = [data.pop(0), data.pop(0)]
    houses = []
    for i in range(0, 2*(N), 2):
        # 감싸주는 것만으로도 인자를 하나라고 인식함
        houses.append((data[i],data[i+1]))
        # 가장 큰 값을 표현할 때
    data_all = [company] + houses + [home]
    minn = float('inf')
    perm(N,0)
    print("#{} {}".format(tc+1, minn))

print(time.time() - start_time, 'seconds')