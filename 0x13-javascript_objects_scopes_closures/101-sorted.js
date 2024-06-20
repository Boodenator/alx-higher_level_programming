#!/usr/bin/node
const dict = require('./101-data').dict;
const newDictn = {};

for (const key in dict) {
  if (!newDictn[dict[key]]) {
    newDictn[dict[key]] = [key];
  } else {
    newDictn[dict[key]].push(key);
  }
}

console.log(newDictn);
