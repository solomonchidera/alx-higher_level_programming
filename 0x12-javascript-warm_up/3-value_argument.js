#!/usr/bin/node
const argument = process.argv.slice(2);
const output = argument.length;

if (output === 0) {
  console.log('No argument');
} else {
  console.log(argument);
}