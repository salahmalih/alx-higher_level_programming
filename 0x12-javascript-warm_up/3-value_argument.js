#!/usr/bin/node
const { argv } = require('node:process');
let i = 0;
if (argv.length > 2) {
  for (i = 2; i < argv.length; i++) {
    console.log(argv[i]);
  }
} else { console.log('No argument'); }
