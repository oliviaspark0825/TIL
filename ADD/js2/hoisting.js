// let 블록 스코프 예제
// var 함수
{
    let x = '정운지'
    console.log(x) // 정운지
    {
        let x = 1
        console.log(x) // 1
    }
    console.log(x) // 정운지
}
console.log(typeof x) // undefined

//  전역변수의 오염
{
    var x = '정운지'
    console.log(x) // 정운지
    {
        var x = 1
        console.log(x) // 1
    }
    console.log(x) // 1
}
console.log(typeof x) // number

let foo
let bar = undefined

foo // undefined
bar // undefined

// baz // reference error baz is not defined



// asda
// asdasd
// let x = 1

// 우리가 쓴 코드
// y
// var y = 1
// y

// js 가 이해한 코드 : 선언만 하고, 할당하지 않음
// var y
// y
// y = 1 // undefined
// y

// if (x !==1) {
//     console.log(y) // undefined y 가 끌어올려져서 인식됨
//     var y = 3
//     if (y ===3 ){
//         var x = 1
//     }
//     console.log(y)  // 3
// }
// if (x === 1 ){
//     console.log(y) // 3
// }

// var 로 변수 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다
var x = 1 // 같은 스코프로 보고 있기 때문에 함수
// var x
// x = 1 이라고 해도 위 var x 에서 한번만 선언된거고, 나중에 x=2가 들어감
if (x ===1) {
    var x = 2
    console.log(x) // 2
}
console.log(x) // 2

// 함수 호이스팅
// ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태
ssafy()
function ssafy() {
    console.log('hoisting!!')
}

// 함수가 들어간 변수라서 안됨
// let ssafy = function(){
//     console.log('hoisting!!')
// }

