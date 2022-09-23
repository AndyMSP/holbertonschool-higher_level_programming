#!/usr/bin/node

const fs = require('fs');
const path = require('path');

// fs.writeFile('content.txt', 'this is the content', (err) => {
//     if (err) throw err;

//     console.log('file created!')
// });

text = fs.readFile('contecnt.txt', 'utf8', (error, data) => {
    console.log(error);
    console.log(data)
});