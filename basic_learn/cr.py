# 숫자 구성된 리스트에서 양의 정수의 합을 구하는 함수 positive_sum을 작성하세요.
def positive_sum(nums):
    ans = 0
    for num in nums:
        if num >0:
            ans += num
    return ans

print(positive_sum([1,-4,7,12]))



# 주어진 문자열에서 소문자 모음을 제거하는 함수 shortcut을 작성하세요.

def shortcut(words):
    ans = ''
    vowel = 'aeiou'
    for word in words:
        if word not in vowel:
            ans += word
    return ans


print(shortcut('goodbye'))


# 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수 start_end를 작성하시오.

def start_end(words):
    # cnt = 0
    # for line in lines:
    #     if len(line) >= 2 and line[0] == line[-1]:
    #         cnt += 1
 

    
    return len([word for word in words if len(word) >= 2 and word[0] == word[-1]])

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))