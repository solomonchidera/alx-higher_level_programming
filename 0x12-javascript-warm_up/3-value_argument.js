#!/usr/bin/node
const [, , firstArg] = process.argv;

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
