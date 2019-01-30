'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
'''

import sys
sys.stdin = open("6.부분집합합.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1,13))
    count = 0



    # 부분집합 만들기
    for i in range(1 << len(A)):
        sum = 0

        sub_A = []
        for j in range(len(A)):
            if i & (1 << j):
                sum += A[j] # 1,2,3을 더하기
                sub_A.append(A[j])
        # print(sub_A)
        # print(sum)
        if sum == K and len(sub_A) == N:
            count +=1





    print("#{} {}".format(tc, count))