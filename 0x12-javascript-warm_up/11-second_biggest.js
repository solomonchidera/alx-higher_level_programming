#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert arguments to integers
const sortedArgs = args.sort((a, b) => b - a); // Sort arguments in descending order

if (sortedArgs.length < 2) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
}
