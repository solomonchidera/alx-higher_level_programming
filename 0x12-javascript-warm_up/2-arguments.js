#!/usr/bin/node
const args = process.argv.slice(2);
const output = args.length;

if (output === 0) {
    console.log("No argument");
} else if (output === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}