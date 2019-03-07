import sys
sys.stdin = open('덧셈.txt')
S, X = input().split()

# for i in range(1,len(S)):
#     if int(S[:i]) + int(S[i:]) == int(X):
#         print("{}+{}={}".format(int(S[:i]), int(S[i:]), X))
#         break
# else:
#     print('NONE')

N = len(S)
#3개를 만들기
for i in range(len(S)-3+1): # A 정수 제어
    for j in range(i+1,len(S)-1): # B 정수 제어
        print("{} {} {}".format(int(S[:i]) + int(S[i:j]) + int(S[j:])))

# for i in range(N):
#     for j in range(i,N-1):
#     A = S[:i]
#     B = S[i:j]
#     C = S[j:]
#
#
# for i in range(N-2):
#     A = int(S[:i+1])
#     for j in range(i+1,N-1):
#         B = int(S[i:j])
#         C = int(S[j:])
#         print(A,B,C)