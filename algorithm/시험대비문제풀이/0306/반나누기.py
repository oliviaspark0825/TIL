import sys
sys.stdin = open('반나누기.txt')
T = int(input())
for i in range(1):
    N, k_min, k_max = [int(i) for i in input().split()]
    test_score = list(map(int,input().split()))
    test_score.sort()
    print(test_score)
    max = 0
    min = 101
    scorelist = [0]*(N+1) # 점수 갯수 분포테이블
    score = sorted(list(set(test_score)))
    print(score)
    # 점수에 따라서 명수를 체크했음
    for s in range(len(test_score)):
            scorelist[test_score[s]]+=1
    # 점수테이블에서 0이 아닌 점수가 3개 이상일경우, 그 사이를 기준으로 나누면 됨
    # for t in range(len(scorelist)):
    #     if scorelist[t] != 0:
    #         score.append(t)
    #     score.sort()
    # # print(score)

    if len(score)>=3:
        T1 = score[-1]
        T2 = score[-2]
    A = 0
    B = 0
    C = 0
    classes = {'A':0, 'B':0, 'C':0}
    max_c = 0
    min_c = 101
    # 학생을 점수에 따라 나누기
    # for i in range(N):
    #     if test_score[i] >= T1:
    #         classes['A'] += 1
    #     elif T2<=test_score[i]<T1:
    #         classes['B'] += 1
    #     else:
    #         classes['C'] += 1
    #
    # for i in classes:
    #     if classes[i]> max_c:
    #         max_c = classes[i]
    #     if classes[i]< min_c:
    #         min_c = classes[i]
    # # print(classes)
    # # 반별 사람 수가 k_min 보다 적으면 탈락
    # for i in classes:
    #     if classes[i] < k_min:
    #         print (-1)
    #         break
    # else:
    #     print(max_c - min_c)

