#!/usr/bin/node
const fs_lib = require('fs');
fs_lib.readFile(process.argv[2], 'utf8', function (error, content) {
	console.log(error || content);
});

