# 반복문자 지우기
import sys
sys.stdin = open("반복문자지우기.txt")
T = int(input())

for tc in range(T):
    text = list(input())
    # print(text)
    dump = []
    for i in range(len(text)):
        if len(dump) == 0:
            dump.append(text[i])
        else:
            if dump[-1] != text[i]:
                dump.append(text[i])
            else:
                dump.pop(-1)

    ans = len(dump)

    print("#{} {}".format(tc+1, ans))


