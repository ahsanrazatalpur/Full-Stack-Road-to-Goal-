// Working with files and Path modules

// FS modules How to read files through it 

// "npm init -y" command to initailize any node project



import fs from "fs";

console.log(fs);


console.log("Starting"); // first thisn run
fs.writeFileSync("Ahsan.txt", "Hey Im ahsan"); // This 2ndly this run
fs.writeFile("Ahsan2.txt", "Hey Im ahsan From txt 2 ", () => {
    console.log("Done")
    fs.readFile("Ahsan2.txt", (error, data) => {
        console.log(error, data.toString)
    })
}); // This 2ndly this run
console.log("Ending"); // lastly this run
// Again
// console.log("Starting"); // first thisn run
// fs.writeFileSync("Ahsan.txt", "Hey Im ahsan"); // This 2ndly this run
// fs.writeFile("Ahsan2.txt", "Hey Im ahsan From txt 2 ", () => {
//     console.log("Done")
//     fs.readFile("Ahsan2.txt", (error, data) => {
//         console.log(error, data.toString)
//     })
// }); // This 2ndly this run
// console.log("Ending"); // lastly this run
// // Again
// console.log("Starting"); // first thisn run
// fs.writeFileSync("Ahsan.txt", "Hey Im ahsan"); // This 2ndly this run
// fs.writeFile("Ahsan2.txt", "Hey Im ahsan From txt 2 ", () => {
//     console.log("Done")
//     fs.readFile("Ahsan2.txt", (error, data) => {
//         console.log(error, data.toString)
//     })
// }); // This 2ndly this run
// console.log("Ending"); // lastly this run
// // Again


