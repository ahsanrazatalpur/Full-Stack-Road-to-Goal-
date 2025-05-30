// Array  collection of mutilple datatype 
// Array is mutable

let arr = [1 ,2 ,3 ,4, 5]
console.log(arr)
console.log(typeof(arr))
console.log(arr.length)

console.log(arr[0])
console.log(arr[1])
console.log(arr[2])
console.log(arr[3])
console.log(arr[4])

arr[0] = 55
console.log(arr[0])

console.log(arr)

// to convert array to string  .toString()
console.log(arr.toString())

// .join  to join and string or value to array
const a = ' and '
console.log(arr.join(a))

// pop(value) by default last value
arr.pop()
console.log(arr)
arr.pop(1)
console.log(arr)

// push(value)  any value in the last
const b = [10, 20, 30 ,40]
console.log(b.push(50))
console.log(b.push('Ahsan'))
console.log(b.push(true))
console.log(b)

//.shift() remove first element
const b2 = [10, 20, 30 ,40]
console.log(b2.shift()) // return shift(first removed value)

// umfhift add value at first
const name = ['ali','ahsan','gull']
console.log(name.unshift('Ahsan'))




