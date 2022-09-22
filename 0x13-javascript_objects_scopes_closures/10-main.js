#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(1));
console.log(myConverter(20));
console.log(myConverter(36));


myConverter = converter(36);

console.log(myConverter(1));
console.log(myConverter(20));
console.log(myConverter(35));