#!/usr/bin/node

// Include process module
const process = require('process');

const av = process.argv;

if (av[2] !== undefined) {
  console.log(av[2]);
} else {
  console.log('No argument');
}
