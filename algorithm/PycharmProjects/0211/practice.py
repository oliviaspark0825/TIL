# 양의 정수의 합 구하기
def positive(numbers):
    ans = 0
    for num in numbers:
        if num > 0:
            ans += num
    return ans

print(positive([4, -1, -100, 6]))



#소문자 제거

def nonvowel(words):
    vowel = ['a', 'e', 'i', 'o', 'u']
    new = []

    for word in words:
        if word not in vowel:
            new.append(word)

    return ''.join(new)

words = 'i love newyork'
print(nonvowel(words))


# 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수 start_end를 작성하시오

def same(word):

    if len(word) >= 2:
        cnt = 0
        for i in range(len(word)):
            if word[1] == word[-1]:
                cnt += 1

