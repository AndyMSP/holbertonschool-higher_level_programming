#!/usr/bin/node

const process = require('process');
const av = process.argv;

function fact (x) {
  if (!(x >= 1)) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}

console.log(fact(av[2]));
