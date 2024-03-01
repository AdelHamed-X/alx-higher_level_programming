#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (h, w, size) {
    super(h, w);
    this.size = size;
  }
}

module.exports = Square;
