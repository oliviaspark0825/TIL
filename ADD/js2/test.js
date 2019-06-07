var y
var x

if (x !==1) {
    console.log(y) // undefined y 가 끌어올려져서 인식됨
    var y = 3
    if (y ===3 ){
        var x = 1
    }
    console.log(y)  // 3
}
if (x === 1 ){
    console.log(y) // 3
}