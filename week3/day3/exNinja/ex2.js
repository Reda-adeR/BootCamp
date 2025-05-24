function capitalize(str) {
  let even = '';
  let odd = '';
  for (let i = 0; i < str.length; i++) {
    even += i % 2 === 0 ? str[i].toUpperCase() : str[i];
    odd  += i % 2 !== 0 ? str[i].toUpperCase() : str[i];
  }
  return [even, odd];
}

console.log(capitalize("abcdef"));
