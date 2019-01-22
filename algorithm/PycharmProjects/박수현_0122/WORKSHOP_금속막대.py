import sys
sys.stdin = open("금속막대.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bolt = [[0 for _ in range(2)] for _ in range(2)]
    bolt = list(map(int, input().split()))

    for i in range(1, len(bolt)):
        if bolt[i] == bolt[i-1]:
            break
        else:
            


    for i in range(len(bolt)):
        if i % 2 == 0: # 인덱스가 짝수이면

    for i in range(1, len(bolt)+1):
        if bolt[i-1] > bolt[i]:
            bolt[i-1], bolt[i] = bolt[i], bolt[i-1]
    print(bolt)
