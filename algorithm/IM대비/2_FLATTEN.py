import sys
sys.stdin = open('flat.txt')
T = 10
for tc in range(T):
     N = int(input())
     data = list(map(int,input().split()))
     i = 1
     while i<=N:
         data.sort()
         data[-1] -= 1
         data[0] += 1
         i+=1
     data.sort()
     diff = data[-1] - data[0]

     print("#{} {}".format(tc+1, diff))


