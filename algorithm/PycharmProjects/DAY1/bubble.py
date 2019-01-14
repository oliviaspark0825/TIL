
     # 리스트 이름은 바뀌지만, 변수는 바뀌지 않음 - 함수한테 복사를 시키면 바뀜
     # 리스트 변수는 참조형이 default 라서 바뀜 함수한테 가면 원본이 바뀜 근데 너무 크니까 걍 원본을 찾아서 빌리라고 함
    # 원본을 참조
     #M = 1 # <-얘는 바뀜
     # COLLECTION - LIST, DICTIONALRY 클래스의 객체

# 내림차순으로 했을 때
# def BubbleSort(data):
#     for i in range(len(data)-1, 0, -1): # 거꾸로 돈다 숫자가 작아지기  n이 두번이니까 O(N**2) 4,3,2,1 4번 돌아요
#         for j in range(0, i): # 5개 까지니까 4까지 돌겠지 까지 돕니다 0~4, 0~3, 0~2  4 3 2 1 #밖의 for 문이 안쪽까지 영향
#              if data[j] > data[j + 1]:
#                 data[j], data[j+1] = data[j+1], data[j]   # swap : 뒤집기  t = a[i] a[i] = a[i+1] a[i+1] = t
# data = [55, 7, 78, 12, 42]
# BubbleSort(data)





def BubbleSort(data):
    for i in range(len(data)-1, 0, -1): # 거꾸로 돈다 숫자가 작아지기  n이 두번이니까 O(N**2) 4,3,2,1 4번 돌아요
        for j in range(0, i): # 5개 까지니까 4까지 돌겠지 까지 돕니다 0~4, 0~3, 0~2  4 3 2 1 #밖의 for 문이 안쪽까지 영향
             if data[j] < data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]   # swap : 뒤집기  t = a[i] a[i] = a[i+1] a[i+1] = t
data = [55, 7, 78, 12, 42]
BubbleSort(data)
print(data)

data = [55, 7, 78, 12, 42]
data.sort()
print(data)



