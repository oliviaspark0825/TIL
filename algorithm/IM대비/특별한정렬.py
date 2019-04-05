import sys
sys.stdin = open('특별한정렬.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    maxx = 0
    minn = 0
    a.sort()

    cnt = 0
    i =0
    j = N-1
    new = []
    new2 = [0]*10
    # for cnt in rnage(N):
    while cnt < 10:
        if cnt % 2 ==0:
            # new.append(a[j])
            new2[cnt] = a[j]
            j -= 1
        else:
            # new.append(a[i])
            new2[cnt] = a[i]
            i +=1
        cnt+=1
    print('#{}'.format(tc+1), end=' ')
    print(*new2)