'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}


function minimumAbsoluteDifference(arr) {
    arr.sort(function (a, b) { return a - b; })
    var i, rv;
    for (i = 1; i < arr.length; i++) {
        if (typeof rv == 'undefined') {
            rv = Math.abs(arr[i] - arr[i - 1]);
            // console.log(rv);
        } else {
            rv = Math.min(rv, Math.abs(arr[i] - arr[i - 1]));
            // console.log(rv);
        }
    }
    return rv;
}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const result = minimumAbsoluteDifference(arr);

    ws.write(result + '\n');

    ws.end();
}
