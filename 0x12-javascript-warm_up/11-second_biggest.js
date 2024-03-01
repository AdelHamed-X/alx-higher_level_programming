#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const sorted = args.sort(function (a, b) {
    return a - b;
  });
  console.log(sorted[args.length - 2]);
}
