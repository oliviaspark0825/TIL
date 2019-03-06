import sys
sys.stdin = open('기본회문.txt', 'r')
N = int(input())
for tc in range(N):
    words = input()
    ans = ''
    for i in range(len(words)//2):
        if words[i] != words[-i-1]:
            ans = 0
            break
        else:
            i += 1
            ans = 1

    print("#{} {}".format(tc+1, ans))

