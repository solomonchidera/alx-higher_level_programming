#!/usr/bin/node
// Get the command-line arguments directly
const [, arg1, arg2] = process.argv;

// Handle undefined cases gracefully using the Nullish Coalescing Operator (??)
console.log(`${arg1 ?? 'undefined'} is ${arg2 ?? 'undefined'}`);
