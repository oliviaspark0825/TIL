import sys
sys.stdin = open('단조증가.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    snum = list(map(int, input().split()))
    L = []
    yes = 0
    no = 0
    z = []
    newL = []
    for i in range(N-1):
        for j in range(i+1,N):
            L.append(snum[i]*snum[j])



    i = 0
    while i<len(L) and L[i] // 10 != 0:
        z = []
        k = i
        temp = L[i]
        z.append(temp // 10)
        temp = temp % 10
        if temp // 10 == 0:
            z.append(temp)

        for s in range(len(z)-1):
            if z[s] <z[s+1]:
                newL.append(L[k])
        i += 1


    for j in range(len(L)):
        if L[j] //10 == 0:
            newL.append(L[j])
    newL.sort()
    # print(newL[-1])
    # for i in range(len(snum)-1):
    #     if snum[i] < snum[i+1]:
    #         yes +=1
    #         L.append(snum[i]*snum[i+1])
    #     else:
    #         no +=1
    # L.sort()
    #
    #
    if newL:
        print("#{} {}".format(tc + 1, newL[-1]))
    else:
        print("#{} {}".format(tc + 1, -1))










    for a in snum:
        while a //10 != 0:

            z.append(a//10)
            a = a % 10
            if a // 10 == 0:
                z.append(a)



  for i in range(len(L)):
        while L[i] // 10 != 0:
            temp = L[i]
            snum.pop(i)
            snum.append(temp // 10)
            temp = temp % 10
            if temp // 10 == 0:
                snum.append(temp)


