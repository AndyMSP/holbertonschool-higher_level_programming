#!/usr/bin/node

const process = require('process');
// const av = process.argv;
const x = Number(Math.floor(process.argv[2]));
// const x = parseInt(av[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('x'.repeat(x));
  }
}
