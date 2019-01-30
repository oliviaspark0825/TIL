
T = int(input())

for test_Case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input(.split())))
    min = data[0] # 굉장히 큰 값을 넣어야 예외 상황이 발생하지 않음
    max = data[0]
    for i in range(1, N):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]





#8 숫자카드
'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.'''
#파이썬은 문자열을 받으면 리스트 안에 들어감





T = int(input())

    c = [0] * 10
    N = int(input())
    data = input()
    for i in range(N):
        c[int(data[i])] += 1 # an

    max_value = c[0]
    max_index = 0

    for i in range(1, 10):
    if max_value < = c[i]:
        max_value = c[i]
        max_index = i

    if c[max_index] <= c[i]
        # d이렇게 하면 한번에 구할 수 있음 인덱스만 있으면


for i in range(N):
    C[int(data[i])] += 1  # 문자열에 있는 문자를 하나씩 숫자로 변환하여 카운팅


# INDEX 만으로 구하는 방법법
maxIndx = 0  # 리스트의 인덱스이므로 -1로 초기화
# maxValue = C[0]
for i in range(1, 10):
    if C[maxIndex] <= C[i]:  # 개수가 같은 경우 더 큰 숫자카드 찾기
        # maxValue = C[i]
        maxIndex = i




#전기버스

def find(data, k, n, m):
    data.insert(0,0)    #출발점 - 맨앞에 삽입
    data.append(n)      #종점 - 맨뒤에 추가
    last = 0            #마지막 충전기
    cnt = 0             #충전횟수
    for i in range(1, m + 2):
        if data[i] - data[i-1] > k :    #충전기 사이가 k보다 멀때
            return 0
        if data[i] > last + k:          #i충전기까지 갈 수 없으면
            last = data[i-1] # 직전꺼에 가서 충전하고 오라
            cnt += 1
    return cnt

import sys
sys.stdin = open("전기버스_input.txt")

T = int(input())
for tc in range(T):
    # K : 한번 충전으로 이동할 수 있는 정류장 수
    # N : 정류장 수
    # M : 충전기 설치된 정류장 번호
    K, N, M = map(int, input().split())  #1 ≤ K, N, M ≤ 100
    data = list(map(int, input().split()))
    print("#{} {}".format(tc+1, find(data, K, N, M)))

    # LIST = REFERENCE TYPE - 너무 커서 복사를 못함 -- 원본을 참조함/ 원본을 바꿀 수 없음
