#!/usr/bin/node

// Include process module
const process = require('process');

const av = process.argv;

const sentence = av[2] + ' is ' + av[3];

console.log(sentence);
