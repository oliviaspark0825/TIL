# k 번만큼 골라서 제일 작은 거를 찾아서 바꾼다, 교환 횟수가 작음
#
# def select(list, k):
#     for i in range(0, k):
#         minInex = for j in range ( i+1, len(list)):
#             if list[minIndex] > list[j]:
#                 minIndex = j
#         list[i], list[minIndex] = list[minIndex], list[i]
#     return list[k -1]


def selectionSort(a):
    for i in range(0, len(a) -1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
            a[i], a[min] = a[min], a[i]


data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)


