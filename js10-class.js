// https://www.hackerrank.com/challenges/js10-class/problem?isFullScreen=true
// My only reason to store this in the repo is to remember this syntax for 
// reduce as a simple way to sum an array.

/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */

class Polygon {
    constructor(arr) {
        this.sides_array = arr;
    }
    perimeter() {
        return this.sides_array.reduce(function (tot, x) { return tot + x });
    }
}





const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
