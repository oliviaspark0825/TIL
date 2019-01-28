# 문자열을 뒤집어 정렬하기
def my_strrev(ary):
    str = list(ary)
    for i in range(len(str) //2):
        t = ary[i]
        str[i] = str[len(str)-1-i] # 맨 뒤에 있는 글자 i 만큼씩 빼면 점점 다가옴
        str[len(ary)-1 -i] = t
    ary = "".join(str)
    return ary


ary = 'abcde'
ary = my_strrev(ary)
print(ary)

s = "Reverse tjos strings"
s = s[-1: 0 : -1]
print(s)




