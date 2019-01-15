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
 */
function vowelsAndConsonants(s) {
    let vowels = [], cons = [];
    const all_vowels = ['a', 'e', 'i', 'o', 'u'];
    let c = '';
    for (var i = 0; i < s.length; i++) {
        c = s[i];
        if (all_vowels.includes(c)) {

            vowels.push(c);
        } else {
            cons.push(c);
        }
    }
    for (var i = 0; i < vowels.length; i++) {
        console.log(vowels[i])
    }
    for (var i = 0; i < cons.length; i++) {
        console.log(cons[i])
    }
}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}