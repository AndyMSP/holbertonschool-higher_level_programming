#!/usr/bin/node
const process = require('process');
const av = process.argv;

const num = parseInt(av[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
