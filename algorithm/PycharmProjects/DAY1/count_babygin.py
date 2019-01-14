num =124123

c = [0] * 12 # 6자리 수로부터 각 자리 수를 추추하여 개수를 누적할 리스트, 0으로 초기화 해서 생성 # i +2 가 있어서 12개까지 생성

for i in range(6):
    c[num % 10] += 1
    num //= 10  # num = num // 10    # 정수를 잘라서 배열에 넣기 // == 몫  456789 을 10으로 나누면 9, 8 , 7, 6, 5, 4 이렇게 나오겠지 while num > 0  정수로 넣기 위해 자름
print(c)

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue # triplet이 두번일 때 continue가 없으면 넘어가버리니까

    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue  # 222 숫자가 연속적으로 있으면 continue  없으면 넘어가버리니까
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("NONONO")
