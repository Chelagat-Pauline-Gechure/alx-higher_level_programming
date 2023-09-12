#!/usr/bin/node
const esrever = (list) => {
  const length = list.length;
  const reversed = [];
  for (let j = length - 1; j >= 0; j--) {
    reversed.push(list[j]);
  }
  return reversed;
};
module.exports = { esrever };
