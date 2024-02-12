#!/usr/bin/node
function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  // Recursive case: compute factorial recursively
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
