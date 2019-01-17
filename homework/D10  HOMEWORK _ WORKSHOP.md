# D10 | HOMEWORK

1. Cascading Style Sheets 2번

2. 1) HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. [ T ]

   2)웹 브라우저는 내장 기본스타일이 있어 CSS가 없어도 작동한다.[ T ] -기본 내장이 있음

   3)자식요소 프로퍼티는 부모의 프로퍼티를 모두 상속받는다. [ F ] - 부모 padding을 자식은 안받음 

3. HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위 : rem

4. 후손 셀렉터와 자식셀렉터

   ```css
   1) div 안에 있는 모든 후손에게 적용됨
   div p {
       color: crimson;
   }
   
   2) div 바로 아래 p에게만 적용됨
   div > p {
       color: crimson;
   }
   
   ```



## D10 | workshop

##### nth- child(n)

* 모든 자식의 순서에서 찾음
* 해당하는 태그의 순서

##### nth-of-type(n)

* 해당하는 자식 태그 요소에서의 순서를 찾음
* 부모 속성에서 특정태그를 가진 자식 속성에서 몇번째에 해당하는지