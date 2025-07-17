// const http = require('node:http'); // Kisi be module ko import krege to require ka use krege
// // const fs = require("fs") // we use import to use module
// // import http from "http"

// const hostname = '127.0.0.1';
// const port = 3000;

// const server = createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/html');
//   res.end('<h1>AHSAN RAZA</h1>');
// });

// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });


// // command to restart server "npm install --global nodemon"
// // to automatically restart  "nodemon filename"


// There are two types of export 
// 1 . Name export(by name)
import {a,b} from "./mymodule" // 1, 2

// 2 . Default export 
import obj from "./mymodule"; //(isko kisi b name se import ker sakte)
console.log(obj);

 
