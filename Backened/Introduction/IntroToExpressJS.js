// // Express JS is with the help of node JS the web developmennt Framework

// import { createServer } from 'http';

// const server = createServer((req, res) => {
//   res.writeHead(200, { 'Content-Type': 'text/plain' });
//   res.end('Hello, world! My Era');
// });

// server.listen(3000, () => {
//   console.log('Server running at http://localhost:3000/');
// });


// // npm i --global nodemon  command to restart server automatically
// npm i express@4 to dewn 4rth version

const express = require('express');

const app = express();
const port = 3000;

// app.get p\or app.post or app.pull app.delete
app.get('/', (req, res) => {
    res.send('Hello World22!');
});
app.get('/:slug', (req, res) => {
    res.send(`Hello ${req.params.slug}`);
});

// app.get('/home', (req, res) => {
//     res.send('Hello World!');
// });

// app.get('/about', (req, res) => {
//     res.send('Hello World!');
// });

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});


