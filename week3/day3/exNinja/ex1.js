const random = Math.floor(Math.random() * 100) + 1;
console.log("Random number:", random);
for (let i = 0; i <= random; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}
