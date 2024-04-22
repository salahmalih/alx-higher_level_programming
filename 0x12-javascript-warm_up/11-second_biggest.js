#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2]) || parseInt(process.argv[2]) === 1) {
  console.log('0');
} else {
  let i = 0;
  let max = 0;
  for (i = 0; i < process.argv.length - 1; i++) {
    if (process.argv[i] < process.argv[i + 1]) {
      max = process.argv[i + 1];
    }
  }
  console.log(max);
}
