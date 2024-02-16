#!/usr/bin/node
const fsLib = require('fs');
fsLib.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});

