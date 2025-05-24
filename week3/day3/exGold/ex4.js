function isOmnipresent(arr, val) {
  return arr.every(subArr => subArr.includes(val));
}

console.log(isOmnipresent([[1,1],[1,3],[5,1],[6,1]], 1));
console.log(isOmnipresent([[1,1],[1,3],[5,1],[6,1]], 6));
