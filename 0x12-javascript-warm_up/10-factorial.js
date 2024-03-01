#!/usr/bin/node

function factorial (a) {
  if (parseInt(a)) {
    return a * factorial(a - 1);
  } else {
    return (1);
  }
}

console.log(factorial(process.argv[2]));
