# python 과거 // 저 %s를 자주 바꾸어야할 때는 뒤의  one two만 바꾸면 됨
'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

#1 pyformat // . for 은 메소드임 (for (args))
#'{} {}'.format( 'one', 'two')

#처음에 오는 name 이 0번인데, 순서 바꾸고 싶으면 {}안에 숫자 넣기 {1}만 두개 쓰면 olivia 만 두번 나오겠지?

name = '빵수수'
e_name = 'Olivia'
print('안녕하세요. {1}입니다. My name is {0}'.format(name, e_name))

#2 f-string python 3.6
print(f'안녕하세요. {name}입니다. My name is {e_name}.')


# LOTTO # sort는 숫자를 순서대로 해주니까 필요하겠지? # random 함수를 불러와야지 얘가 알아듣겠지
import random
x = list(range(1,46))
lotto = random.sample(x,6)
lotto.sort()
print(f'오늘의 행운 번호는 {lotto}입니다.')


#3 
name = '홍길이'
print("안녕하세요. " + name + "입니다.")

# 파일명바꾸기 






