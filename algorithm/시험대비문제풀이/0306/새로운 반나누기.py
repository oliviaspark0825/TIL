import sys
sys.stdin = open('반나누기기.txt')
T = int(input())
for i in range(T):
    N, k_min, k_max = [int(i) for i in input().split()]
    test_score = list(map(int,input().split()))
    test_score.sort()
    score = sorted(list(set(test_score))) # 점수 나온거
    pass_class = []

    for T1 in range(1, (score[-1]+1)):
        for T2 in range(T1+1,(score[-1]+1)):
            #학생을 점수에 따라 나누기

            classes = {'A': 0, 'B': 0, 'C': 0}
            for i in test_score:
                if i >= T2:
                    classes['A'] += 1
                elif T1<=i<T2:
                    classes['B'] += 1
                else:
                    classes['C'] += 1
            max_c = 0
            min_c = 99999
            for i in classes:
                if classes[i]> max_c:
                    max_c = classes[i]

                if classes[i]< min_c:
                    min_c = classes[i]

            # 반별 사람 수가 k_min 보다 적으면 탈락
                if max_c <= k_max and min_c >= k_min:
                    ans = max_c - min_c

                    pass_class.append(ans)
        # print(pass_class)
    # 최소 최대 나눈
    print(pass_class)
    if pass_class:
        print(min(pass_class))
    else:
        print(-1)
