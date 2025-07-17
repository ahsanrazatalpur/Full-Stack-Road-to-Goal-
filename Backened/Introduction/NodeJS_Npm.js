// Time to move on JavaScript Backend Rather than run in Script(frontend)
// Step 1  : Download Node JS LTS version Bits according to your pc
// after downlaod completion use VS code and open terminals use the following commands to check npm node version 
//  node --version (to check node version)  , npm --version (to check npm version)
// If we make a backend project we shoud use Node JS
// to type any line on node use console.log("hello"); or type line and run command node .\server.js to run the program

console.log("Hello, Wolrd");

// // is we want to maintain our project or the work for a long time we should initialize it as npm project commands are
// 1. npm init  
// 2. name the project
// 3. tell the version by default 0.0.1
// 4. now tell the description about your project 
// 5. entery point server.js
// 6. skip test command
// 7. skip git repo
// 8. keyword eg spotify music 
// 9. author : our name
// 10. licence  leave it blank
// and then press yes now you see package.json file has created

// now we have run this prgram as npm project now we install different package and we already initialize it as single entity 

// Example : we now install slug package
// command  is " npm i slugify"

// now the node modules folder has been create

// Node JS is nothiing but JS and Chrome v8 engine 

// Example Slugify(url like text remove space and some invalid character)

var slugify = require('slugify')

let a = slugify('some string') // some-string
console.log(a)

const b = slugify('some string', '_')
console.log(b);