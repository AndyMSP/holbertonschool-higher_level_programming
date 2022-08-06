#!/usr/bin/node

const process = require('process');
const av = process.argv;

av.splice(0, 2);

for (const i in av) {
  av[i] = parseInt(av[i]);
}

av.sort((a, b) => b - a);

if (av.length < 2) {
  console.log(0);
} else {
  console.log(av[1]);
}
