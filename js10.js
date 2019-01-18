// Code for Hackerrank's 10 days of JS tutorial

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * This can probably be made less clumsy but it works.
 * https://www.hackerrank.com/challenges/js10-loops/problem
 */
function vowelsAndConsonants(s) {
    let vowels = [], cons = [];
    const all_vowels = ['a', 'e', 'i', 'o', 'u'];
    let c = '';
    var i;
    for (i = 0; i < s.length; i++) {
        c = s[i];
        if (all_vowels.includes(c)) {
            vowels.push(c);
        } else {
            cons.push(c);
        }
    }
    for (i = 0; i < vowels.length; i++) {
        console.log(vowels[i])
    }
    for (i = 0; i < cons.length; i++) {
        console.log(cons[i])
    }
}

function getSecondLargest(nums) {
    nums = nums.sort(function (a, b) {return a-b;});
    let n = nums.length;
    var the_max = nums[n-1];
    for (var i = n - 1; i >= 0; i--) {
        if (nums[i] < the_max) {
            return (nums[i]);

        }
    }
}

function main() {
    // var arr = [2, 3, 6, 6, 5];
    var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    console.log(getSecondLargest(arr));
    // const s = readLine();
    // const s = "helloworldhowareyou";
    // vowelsAndConsonants(s);
}

main();