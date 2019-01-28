num_rule = ['ZRO', 'ONE', 'TWO','THR', "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
L = []
for s in range(10):
    L.append(num_rule[s])
print(L)
print(num_rule[0])


import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for tc in range(T):
    temp = input() # dummy
    data = list(map(str,input().split()))

    C = [0] * 10
    result = ''

    num_rule = ['ZRO', 'ONE', 'TWO','THR', "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in range(len(data)):
        for j in range(len(num_rule)):
            if data[i] == num_rule[j]:
                C[j] += 1

    for s in range(10):

        result += ((num_rule[s] + " ") * C[s])

    print("#{} {}".format((tc+1), result))
