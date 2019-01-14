
# for i1 in range(1, 4, 1): # 배열이었으며 0 부터도 가능, 지금은 숫자니까 # 1,
#     for i2 in range(1, 4):  # 2 3 (1이 이미 나왔으면)
#         if i2 != i1:
#             for i3 in range(1, 4): # 3
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)

# data = [6, 6, 7, 7, 6, 7] # index 값으로 순열 만들기 데이터 (6 이런 숫자)는 따로 있고
# for i1 in range(len(data): # 배열이었으며 0 부터도 가능, 지금은 숫자니까 # 1,
#     for i2 in range(6):  # 2 3 (1이 이미 나왔으면)
#         if i2 != i1:
#             for i3 in range(6): # 3
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)
#
# data = [6, 6, 7, 7, 6, 7] # index 값으로 순열 만들기 데이터 (6 이런 숫자)는 따로 있고
# for i1 in range(3): # 배열이었으며 0 부터도 가능, 지금은 숫자니까 # 1,
#     for i2 in range(3):  # 2 3 (1이 이미 나왔으면)
#         if i2 != i1:
#             for i3 in range(3): # 3
#                 if i3 != i1 and i3 != i2:
#                     print(data[i1], data[i2], data[i3])  # index 값으로 표현

def babyGin(data):

# data = [6, 6, 7, 7, 6, 7]  # index 값으로 순열 만들기 데이터 (6 이런 숫자)는 따로 있고
    for i1 in range(6):  # 배열이었으며 0 부터도 가능, 지금은 숫자니까 # 1,
        for i2 in range(6):  # 2 3 (1이 이미 나왔으면)
            if i2 != i1:
                for i3 in range(3):  # 3
                    if i3 != i1 and i3 != i2:
                        for i4 in range(6):  # 배열이었으며 0 부터도 가능, 지금은 숫자니까 # 1,
                            if i4 != i1 and i4 != i2 and i4 != i3:
                                for i5 in range(6):  # 3
                                    if i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:
                                        for i6 in range(6):
                                            if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5:
                                                chk = 0
                                                if data[i1] == data[i2] and data[i2] == data[i3]:
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i5] == data[i6]:
                                                    chk += 1
                                                if data[i1] +1 == data[i2] and data[i2] +1 == data[i3]:
                                                    chk += 1
                                                if data[i4] +1 == data[i5] and data[i5] +1 == data[i6]:
                                                    chk += 1
                                                if chk == 2:
                                                    return True


data = [6, 6, 7, 7, 6, 7]
babyGin(data) # 함수 안쓰면 계속 돌아가니까
if babyGin(data):
    print("Baby Gin")
else:
    print("not FALSE!")
