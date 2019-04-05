import sys
sys.stdin = open('특별한정렬.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    maxx =0
    minn = 0
    for i in range(N):
        if i % 2 == 0:  # index가 짝수이면 max 수를 넣으세요
            maxx = i  # 선택정렬로 제일 작은 수 뽑아내기
            for k in range(i + 1, len(a)):
                if a[maxx] < a[k]:
                    maxx = k
            a[i], a[maxx] = a[maxx], a[i]
        else:  # index가 홀수이면 min 넣기
            minn = i
            for s in range(i + 1, len(a)):  # 선택정렬로 제일 작은 수 뽑아내기
                if a[minn] > a[s]:
                    minn = s
            a[i], a[minn] = a[minn], a[i]

    new_a = a[0:10]
    # print(new_a)
    new_a = ' '.join(map(str, new_a))

    print("#{} {}".format(tc, new_a))
