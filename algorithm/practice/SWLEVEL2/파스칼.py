import sys
sys.stdin = open('파스칼.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    # pascal = [0] * 11 # 어차피 숫자의 길이가 최대 10개니까
    L = [1]
    for i in range(1,N+1):
        for j in range(i+1):
            if i < 2:
                print(L[j], end=' ')
                L.append(1)

            else:
                x = len(L)
                for j in range(i + 1):
                    if j == 0 or j == i:
                        print(1, end=" ")
                        L.append(1)
                    else:
                        print(L[j - 1] + L[j], end=" ")
                        L.append(L[j - 1] + L[j])
                for j in range(x):
                    L.pop(0)
            print()