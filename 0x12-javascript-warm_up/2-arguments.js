#!/usr/bin/node

const { argv } = require('node:process');

// print process.argv
//argv.forEach((val, index) => {
//  console.log(`${index}: ${val}`);
//});

if(process.argv.length <= 2){
	console.log("No argument");
} else {
	console.log("Argument found");
}
