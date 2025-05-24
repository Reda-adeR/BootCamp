function biggestNumberInArray(arr) {
  const nums = arr.filter(x => typeof x === "number");
  return nums.length ? Math.max(...nums) : 0;
}

console.log(biggestNumberInArray([-1,0,3,100,99,2,99]));
console.log(biggestNumberInArray(['a', 3, 4, 2]));
console.log(biggestNumberInArray([]));
