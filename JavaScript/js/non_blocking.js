// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000) // non-block  callback stack 얘가 비동기로 돌고있어서
// console.log('end of program')


//  python code 처럼 동작하게 하려면
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000) // call back 함수에 얘를 넣어버리면
// 3초뒤에 실행이 되어버리니까


// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }
// first()
// setTimeout(second, 5000) // 이벤트 루프 - 시간의 흐름에 따라 코드의 수행을 처리하고,

// 아무리 0초라도, callback stack으로 보내버림과 동시에 third가 실행되기 때문에
// 일단 callback에 보내져야 하기에
// third()

 // func1()를 호출했을 때 아래와 같이 콘솔에 출력
function func1() {
    console.log('func1')
}
function func2() {
    console.log('func2')
}
function func3() {
    console.log('func3')
}
func1()
setTimeout(func2, 3000)
func3()

function func1() {
    console.log('func1')
    func2()
}
function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}
function func3(){
    console.log('func3')
}
func1()

