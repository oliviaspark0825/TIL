# import sys
# sys.stdin = open('배부른돼지.txt', 'r')
N = int(input())
if N == 0 :
    print('F')
else:
    yes = []
    no = []
    min = 10
    max = 2
    data = [tuple(input().split()) for _ in range(N)]
    for i in range(len(data)):
        if data[i][1] == 'Y':
            yes.append(data[i][0])

        if data[i][1] == 'N':
            no.append(data[i][0])
    yes.sort()
    no.sort()
    min = yes[0]
    max = no[-1]

    if max < min:
        print(min)
    else:
        print('F')


N = int(input())
Ymin = 9
Nmax = 2
if N==0:
    print('F')
else:
    for i in range(N):
        cnt, yn = input().split()
        cnt = int(cnt)
        if yn is 'Y':
            if Ymin > cnt: Ymin = cnt
        else:
            if Nmax < cnt : Nmax = cnt
    if Nmax < Ymin:
        print(Ymin)
