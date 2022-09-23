#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const file = process.argv[2];

function callback (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
}

fs.readFile(file, 'utf8', callback);
