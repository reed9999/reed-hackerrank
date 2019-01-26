// See https://www.hackerrank.com/challenges/new-year-chaos/problem
// Successfully (sorta) ported my Python implementation to JS, but like Python it still fails
// some long tests that time out. Since it's doing a lot of unneccessary sorts, that's
// probably not surprising.



'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function minimumBribes(q) {
    if (testForChaos(q)) {
        console.log("Too chaotic");
        return "CHAOS!";
    }
    let rv = minimumBribes_impl(q, 0);
    console.log(rv);
    return rv;
}


function minimumBribes_impl(q, subtotal) {
    for (var i=1; i <= q.length; i++) {
        var original = q[i-1];
        if (i == original) {
            continue;
        }
        var remainingArray = q.slice(i);
        return minimumBribes_impl(normalize(remainingArray), subtotal + original - i);
    }
    return subtotal;
}

function normalize(q,) {
    var rv = [];
    var sorted_q = q.slice(0).sort(function(a, b) {return a - b;})
    for (var item of q) {
        rv.push(sorted_q.indexOf(item)+1);
    }
    return rv;
}


function testForChaos(q) {
    for (var i=1; i <= q.length; i++) {
        if (q[i-1] - i > 2) {
            return true;
        }
    }
    return false;
}


function main() {
    console.log("hello")
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4, ]);
}

function standardMain() {
    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine(), 10);

        const q = readLine().split(' ').map(qTemp => parseInt(qTemp, 10));

        minimumBribes(q);
    }
}


main();

// # TC 7 times out. Expected value is:
// # 115173
// # Too chaotic
// # 115013
// # Too chaotic
