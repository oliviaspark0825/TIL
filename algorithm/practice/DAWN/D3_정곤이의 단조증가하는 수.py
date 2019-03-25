import sys
sys.stdin = open('단조증가.txt')
T= int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    multiple = []
    for i in range(N-1):
        # 항상 j가 커야하니까
        for j in range(i+1,N):
            multiple.append(nums[i]*nums[j])
    # print(multiple)
    answers = []
    # 자릴수를 나눈 것을 차례로 넣어서, 0,1,2, 순서대로 숫자의 크기가 크면 통과
    for i in multiple:
        rst = i
        divide_r = []
        while i != 0:
            divide_r.append(i % 10)
            i = i //10
        for i in range(len(divide_r)-1):
            if divide_r[i] < divide_r[i+1]:
                break
            else:
                answers.append(rst)
    maxx = -9876654
    for a in answers:
        if a > maxx:
            maxx = a


    print('#{} {}'.format(tc+1, maxx))









    # % , // 이용해서 자릿수 자르기