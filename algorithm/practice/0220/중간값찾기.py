# import sys
# sys.stdin = open('중간값.txt', 'r')
# N = int(input())
# for tc in range(N):
#     data = list(map(int, input().split()))
#     print(data)
#     new = []
#     for i in range(len(data)):
#         min = data[0]
#         if data[i] < min:
#             new.append(data[i])
#     print(new)



def maxline(k):
    for i in range(len(k)):
        for j in range(0, len(k)-i): # k번이면 k-1 까지 돌아야 하니까 갯수를 하나씩 줄여야지
            if k[j] > k[j + 1]:
                k[j], k[j + 1] = k[j + 1], k[j]
    return k

a = [10, 1, 25, 40, 7, 5]
print(maxline(a))

    for i in range(len(k)):
        if k[i] > k[i+1]:
            k[i], k[i+1] = 

