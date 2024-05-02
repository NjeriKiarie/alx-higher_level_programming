#!/usr/bin/node
// A square class that defines a square and inherits from Rectangel of 4-rectangle.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
}

module.exports = Square;
