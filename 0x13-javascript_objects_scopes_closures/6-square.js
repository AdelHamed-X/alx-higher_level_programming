#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
    this.charPrint = function (c) {
      for (let i = 0; i < size; i++) {
        console.log(c ? 'C'.repeat(size) : 'X'.repeat(size));   
      }
    }
  }
}

module.exports = Square;
