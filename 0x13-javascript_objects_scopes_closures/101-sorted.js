#!/usr/bin/node
const dict = require('./101-data').dict;
const myDictn = {};

for (const key in dict) {
  if (!myDictn[dict[key]]) {
    myDictn[dict[key]] = [key];
  } else {
    myDictn[dict[key]].push(key);
  }
}

console.log(myDictn);
