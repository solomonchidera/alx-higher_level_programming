#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        // If w or h is 0 or not a positive integer, create an empty object
        return {};
      }
      // Initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    }
  
    // Instance method to print the rectangle using the character X
    print() {
      if (!this.width || !this.height) {
        console.log("Empty Rectangle");
        return;
      }
  
      // Print the rectangle using X
      for (let i = 0; i < this.height; i++) {
        let row = "";
        for (let j = 0; j < this.width; j++) {
          row += "X";
        }
        console.log(row);
      }
    }
  }

module.exports = Rectangle;