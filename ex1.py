# 1
# 다음 리스트의 요소들을 한줄로 출력하시오
numbers = [2,3,6,11,8]
# for 문 사용.

#for a in list(numbers):
 
numbers = [2,3,6,11,8]
for i in numbers:
    print(i,end =" ")








# 2
# 주어진 리스트의 요소들 중에서 자연수가 홀수인지 짝수인지 판별하여 각각의 리스트로 출력하여라.

numbers = [1, 2, 3, 4, 5, 6, 7,8,9,10]
int a = 0
a = numbers
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")


# answers  []를권장
numbers = [1, 2, 3, 4, 5, 6, 7,8,9,10]
odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even, "짝수입니다")
print(odd, "홀수입니다")