/* var hello = name => "hello" + name
console.log(hello)
var people = (name, age) => {
    const fullName = "hello" + name
    return fullName
}

var calculate = (x, y, z) => {
    if (typeof x != 'number') { x = 0 }
    if (typeof y != 'number') { y = 6 }
    var dwt = x % y
    var result
    if (dwt == z) { result = true }
    if (dwt != z) { result = false }
    return result
} */
const calculate = (x, y, z) => {
    x = typeof x !== 'number' ? 0 : x
    y = typeof y !== 'number' ? 6 : y
    return x % y === z
}
calculate(3,4,5)