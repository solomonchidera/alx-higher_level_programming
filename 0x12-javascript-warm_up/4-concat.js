#!/usr/bin/node
const [arg1 = 'undefined', arg2 = 'undefined'] = process.argv.slice(2);
console.log(`${arg1} is ${arg2}`);
