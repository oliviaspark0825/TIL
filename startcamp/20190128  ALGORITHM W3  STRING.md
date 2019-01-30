# 20190128 | ALGORITHM W3 | STRING

문자열

패턴매칭

#### ASCII -  0 : \o / 7bit 인데? 

영문자 한개는 1byte인데 7비트임, 127까지만 있음  7bit + 1bit = parity  bit : 에러를 검출한다(수정 x)

parity - even, odd

압축했을 때 풀다가 crc check 깨지는거 방지하기 위해서 - 원본 대조

확장 아스키는 표준 아님

#### 유니코드

 2	바이트 - 근데 그거 넘어가면 읽는데 문제 발생\

8자리를 한번에 읽을 것인가 or 2개로 나눌 것인가



#### 숫자표현

- 정수와 실수로 나누어야
- 음수는 2의 보수를 사용 -  +1을 하면 2의 보수
- 실수 = 

### unicode

UCS-2

UCS-4

UTF-8 8개씩 잘라서 읽는다 / 웹에서 사용

big - endian / little - endian

0x1234 - 2바이트 16진수 2자리 == 1바이ㅡ

0x1234 - 34 / 12  little endian 작은게 뒤로  가게

java - 2byte :유니코드로 저장되어서 -- 그래서 windows 는 16비트로 함 / 영문자는 한자리만 차지하니까 빈자리 하나는 다른거로 채움 

2uc-kr

client side 



python encoding

객체 = 주소값을 가지고 있는 것

char 타입 없음 . 텍스트는 모두 str으로 통일되어 있음

연결 concatenation + *



문자열 비교 

java = equals 메서드 활용

heap - 정적 메모리



list - reference참조형

string - heap 에 저장 정적 / 

파이썬에서는 == 연산자가 내부적으로 특수 메섣ㅡ __eq__ 를 호출

메모리가 두개가 같은지를 물어보는 거임

---



문자열을 뒤집기

문자열 함수를 정수로 변환하기 - c 에서는 tostring

패턴매칭



2) 매칭이 실패했으 때 돌아갈 곳 계산 



