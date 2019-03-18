import sys
sys.stdin = open('마디.txt')
T = int(input())
for tc in range(T):
    pattern = list(input())

    length = 0
    for i in range(len(pattern)-1):
        for j in range(1,len(pattern)-1):
            if pattern[i] == pattern[j] and pattern[i+1] == pattern[j+1]:
                length = j
                break
        if length:
            break
    print('#{} {}'.format(tc+1,length))
