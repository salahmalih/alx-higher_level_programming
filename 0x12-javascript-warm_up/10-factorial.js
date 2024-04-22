#!/usr/bin/node
function fact (a) {
  if (a === 1) {
    return 1;
  }
  return a * fact(a - 1);
}
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('1');
} else {
  console.log(fact(process.argv[2]));
}
