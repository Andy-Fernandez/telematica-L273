// main.js
const reverseModule = require("./reverse");
const argument = process.argv[2];

console.log(reverseModule.reverse(argument));
