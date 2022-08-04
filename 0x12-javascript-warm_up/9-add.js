#!/usr/bin/node

const process = require('process');
const av = process.argv;
const a = parseInt(av[2]);
const b = parseInt(av[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(a, b));
