#!/usr/bin/node
const mySecondBiggest = process.argv;
if (mySecondBiggest.length <= 3) {
  console.log(0);
} else {
  console.log(mySecondBiggest.sort((x, y) => y - x).slice(3)[0]);
}
