time = 125
new = 0
a, b, c = 300, 60, 10
cnt_a = 0
cnt_b = 0
cnt_c = 0
if time // a >= 1:
    cnt_a = time // a
    time = time % a
    print(time)
if time // b >= 1:
    cnt_b = time // b
    time = time % b
    print(time)
if time // c >= 1:
    cnt_c = time // c
    time = time % c
print(time)
if time == 0:
    print(f'{cnt_a} {cnt_b} {cnt_c}')
else:
    print(-1)


print(-1) if time % 10 else print(time//a, time %a //b, time %a %b //c)









