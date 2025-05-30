// String in JS
// string used to store an manipulate the text
// "anytext"
// string is immutable

console.log('Hello, World');

let name = 'Ahsan raza'
console.log(name)


// accesing string thrugh index
console.log(name[0])
console.log(name[1])
console.log(name[2])
console.log(name[3])
console.log(name[4])

// Js is forgiving language through least errro becasue it design to run on browser

// get length of string throgh .length function
console.log(name.length)

let hisname = ' Ahsan raza '
let friend = ' Ali'
console.log('His name is'+hisname+'and his friend name is'+friend)

//accesing variable by ${} template literal (use ` baktic sign in template literal)

console.log(`My name is ${hisname}`)

//ESCAPE SEQUENCE
 // special character with \ with it

// use \""\ to print string in double quote
console.log('My name is \"Ahsan\" raza')

// \n to change new line
console.log('Line 1\nline 2\nline 3')

// use \t for tab some random spaces
console.log('He im\tspace')

//Pre Bulit in function

// .UpperCase() to change sttring in uppercase 
let namee = 'Ahsan Raza'
console.log(namee.toUpperCase())

// .LowerCase to change string in lowercase
let name2 = 'Ahsan Raza'
console.log(name2.toLocaleLowerCase())

// .length to get length of string
console.log(name2.length)

// string slice   .sile(start,end)
nam = 'Ahsan Raza'
console.log(name.slice(1,4));

console.log(name.slice(1)); //skip 0  and print all other

// .replcae('old' ,'new') chnage first occurence only
a = 'im here'
console.log(a.replace('here','there'))
// .concat to merge two string and a string by giving comma
b = 'ahsan'
a = 'harry'
console.log(a.concat(b))
console.log(a.concat(b,'Hi g'))

// .charAt(index) tell the location of character
a = 'harry'
console.log(a.charAt(0))

// .indexOf('a') tell the index of character else return -1
console.log(a.indexOf('a'))
a = 'harry'

//startsWith
a = 'harry'
console.log(a.startsWith('a'))

//endsWith
a = 'harry'
console.log(a.endsWith('a'))


