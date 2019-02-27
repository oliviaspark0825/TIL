T = int(input())
a, b, c = 300, 60, 10
cnt_a, cnt_b, cnt_c  = 0, 0, 0
cnt_a = T //a
T = T % a
cnt_b = T // b
T = T % b
cnt_c = T // c
T = T % c
if T == 0:
    print(cnt_a, cnt_b, cnt_c)
else:
    print(-1)
