r = int(input())
# cnt = 0
# for i in range(r):
#     for j in range(r):
#         if (r-i)**2+(r-j)**2 <= r**2:
#             cnt += 1
# print(cnt*4)
cnt = 0
for i in range(1, r+1):
    for j in range(1, r+1):
        if i*i + j*j <= r*r:
            cnt += 1
print(cnt*4)