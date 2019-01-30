'''내가 counting 해서 one 들어오면 1 증가 시키고, counting sort를 해도 되지
 - 0이 몇번 1이 몇번 -하면 바로 정렬이 되니까

 counting 해서 갯수만큼 찍어내기 '''

import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())
for tc in range(T):
    temp = input() # dummy
    data = list(map(str,input().split()))
    # print(temp)
    # print(data)
    # print(len(data))

    C = [0] * 10
    L = []
    result = ''

    num_rule = ['ZRO', 'ONE', 'TWO','THR', "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in range(len(data)):  # data에서 index 순서대로 돌릴거고
        for j in range(len(num_rule)): # nums에서도 비교해야하니까
            if data[i] == num_rule[j]:
                C[j] += 1 # 해당하는 숫자를 카운트 하기

    # print(C)
    for s in range(10):
        # L.append(num_rule[s])
        result += ((num_rule[s] + " ") * C[s])
    # print(result)
    print("#{} {}".format((tc+1), result))









