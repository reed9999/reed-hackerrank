// See https://www.hackerrank.com/challenges/new-year-chaos/problem
// I want to port my Python implementation to JS

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

// def minimumBribes(q):
//     if test_for_chaos(q):
//         print("Too chaotic")
//         return "CHAOS!"
//      # This might be easier to follow with a list comprehension and/or reduce but it's still pretty
//     # straightforward.
//     rv = minimumBribes_impl(q, 0)
//     print(rv)
//     return rv
//
// def minimumBribes_impl(q, subtotal):
//     # iterator = enumerate(q)
//     # for ix, item in enumerate(q):
//     #     print(ix)
//     #     print(item)
//     for ix, original in enumerate(q):
//         ix += 1     #one-based, not zero-based
//         if ix == original:
//             continue
//         # Eventually rather than a separate test_for_chaos we could test here, probably.
//         return minimumBribes_impl(normalize(q[ix:]), subtotal + (original - ix))
//     return subtotal

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
    for (var item in q) {
        rv.push(sorted_q.indexOf(item)+1);
    }
    return rv;
}

//
// def normalize(q):
//     rv = []
//     sorted_q = sorted(q)
//     # Possible list comprehension
//     for item in q:
//         rv.append(sorted_q.index(item)+1)
//     return rv
//
// def test_for_chaos(q):
//     is_chaotic = any([(original - ix - 1 > 2) for ix, original in enumerate(q)])
//     if (is_chaotic):
//         return True

function testForChaos(q) {
    for (var i=1; i <= q.length; i++) {
        if (q[i-1] - i > 2) {
            return true;
        }
    }
    return false;
}


function main() {
    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine(), 10);

        const q = readLine().split(' ').map(qTemp => parseInt(qTemp, 10));

        minimumBribes(q);
    }
}

// """Key test case
// 8
// 1 2 5 3 7 8 6 4
// Proceed to the 5 in place 3. That's two bribes so count 2. Normalize the remaining array:
// 3 7 8 6 4
// becomes
// 1 4 5 3 2
// Proceed to 4. Count 2 (4 cumulative) leaving 5 3 2 -> 3 2 1.
// Count 2 for the 3 (6 cumul) leaving 2 1 which of course is 1 more.
// """
//
// # TC 7 times out. Expected value is:
// # 115173
// # Too chaotic
// # 115013
// # Too chaotic
//
//
// if __name__ == '__main__':
//     arr = [1, 2, 5, 3, 7, 8, 6, 4,]
//     minimumBribes(arr)
//     exit()
//
//     t = int(input())
//
//     for t_itr in range(t):
//         n = int(input())
//
//         q = list(map(int, input().rstrip().split()))
//
//         minimumBribes(q)
