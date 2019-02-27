def make(num):

    while True: # 조건을 정확히 뭐로 줄지 모를 때 # 14 이면 다시 분리하는거로 가야하니까 while을 한번 더 감싸기
        tot = 0  # 14를 초기화하고 들어가야하니까
        while num: # 0이되면 끝나는거니까
                #len(str(num)) != 1:
            tot += num % 10
            num = num // 10
        if tot < 10:
            return tot
        num = tot # 숫자를 14로 바꿔서 다시 시작해야하니까


import sys
sys.stdin = open('숫자근.txt', 'r')

N = int(input())
data =[]
for i in range(N):
    data.append(int(input()))

data_max=0
sol = 0
for i in range(N):
    sums = make(data[i]) # 숫자근 만들어 합을 구해주는 함수
    # 가장 큰 숫자근이면 해당 정수를 솔루션으로
    if sums> data_max:
        data_max = sums
        sol = data[i] # 솔루션에도 해당하는 정수로 갱신하기


    # 가장 큰 숫자근과 같다면 더 작은 정수를 비교해서
    if data_max == sums:
        if sol > data[i]:
            sol = data[i]
print(sol)


'''
while True:
    temp = list(int, str(num))
    tot = sum(temp)
    if tot < 10 : return tot
    num = tot    
'''

    # 가장 큰 숫자금이 여러개면 - 작은거 출력하라
    # 그냥 % 10 로 나눠서 나머지를 계속 append하고, 다 더하면 되지 않나?