#!/usr/bin/node
const argument = process.argv.slice(2);
const output = argument.length;

if (output > 0) {
  console.log(argument[0]);
} else {
  console.log('No argument');
}