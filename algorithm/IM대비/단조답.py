import sys
sys.stdin = open('단조증가.txt')



def judge(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


def checker():
    global result
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if judge(str(numbers[i] * numbers[j])):
                result += [numbers[i] * numbers[j]]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = []
    checker()
    if result:
        result.sort()
        print("#{} {}".format( tc, result[-1]))
    else:
        print("#{} {}".format(tc, -1))