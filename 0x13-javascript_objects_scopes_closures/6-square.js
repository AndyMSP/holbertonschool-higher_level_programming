#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const size = this.width;
    for (let i = 0; i < size; i++) {
      console.log(c.repeat(size));
    }
  }
}

module.exports = Square;
