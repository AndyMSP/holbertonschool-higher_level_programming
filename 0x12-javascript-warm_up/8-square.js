#!/usr/bin/node

const process = require('process');
const av = process.argv;
const x = parseInt(av[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
