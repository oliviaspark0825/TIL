//1. forEach
// forEach 함수는 아무것도 return 하지 않는다


// ESS
var colors = ['red', 'blue', 'green',]

for ( var i=0; i < colors.length; i++) {
    console.log(colors[i])
}

// ES6+
const COLORS = ['red', 'blue', 'green',]
// 익명함수라 안에 들어가는거
COLORS.forEach(function (color){
    console.log(color)
}) 
// function 지우고 - 소괄호랑 중괄호 줄이고 => 하면 됨
COLORS.forEach(color => console.log(color))

// exercise 1-1 아래 함수에 for를 forEach로 바꾸시오
// function handlePosts() {
//     const posts= [
//         { id:23, title:'daily news'},
//         { id:52, title:'Code City'},
//         { id:105,title:'The Ruby'},

//     ]
//     for (let i =0; i < posts.length; i++) {
//         savePost(posts[i])
        
//     }
// }

// posts.forEach(function(post){
//     savePost(post)
// })

// exercise 1-2 아래코드의 images 배열 안에 있는 정보( height, width)를 곱해 넓이를 구하여
//areas 배열에 저장하는 코드를 forEach 헬퍼를 사용해 작성해보자
const images = [
    {height:10, width:30},
    {height:5, width:100},
    {height:20, width:20},

]
const areas = []
/////////////// answer ////////////////
images.forEach(function(image){
    areas.push(image.height*image.width)
})
console.log(areas)

// 2. map
// map 함수는 새로운 배열을 return 한다 (배열요소를 변형)
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때
// map filter는 모두 사본을 return 하며 원본 배열은 바뀌지 않는다.

const NUMBERS = [1, 2, 3,]
const DOUBLE_NUMBERS = NUMBERS.map(function (number){
    return number *2 
})
//한줄짜리
// const DOUBLE_NUMBERS = NUMBERS.map(number => number *2)

console.log(DOUBLE_NUMBERS)

