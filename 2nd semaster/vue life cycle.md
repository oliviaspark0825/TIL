vue 

hook - 각 단계를 지칭하는것

일부 훅은 서버랑 클라이언트 다되기도함

created / mounted  / updated / destroyed

creation - data를 반응형으로 

mount 가상의 dom이 실제 dom에 부착되고 난 이후에 실행되므로 

data, coumputed, methods watch등 모든 요소에 접근이가능

부모 컴포넌트의 mounted훅은 항상 자식 컴포넌트의 mounted훅 이후에 발생한다는 것

하지만 자식 컴포넌트가 서버에서 비동기로 데이터를 받아오는 경우처럼, 부모의 mounted훅이 모든 자식 컴포넌트가 마운트 된 상태를 보장하지는 않습니다. 따라서 이때는 `this.$nextTick`을 이용한다면, 모든 화면이 렌더링 된 이후에 실행되므로 마운트 상태를 보장할 수 있습니다.



update -- 변경된 data가 적용된 상태/ 데이터를 직접 바꾸면 안되고

destroy



부모 자식

그래프만들때 mounted 불러오면 서버에 부담줄 수 있으니까  cloud function써서 