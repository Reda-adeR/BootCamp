const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter words separated by commas: ", (input) => {
  const words = input.split(',').map(w => w.trim());
  const maxLength = Math.max(...words.map(word => word.length));
  const border = '*'.repeat(maxLength + 4);

  console.log(border);
  for (let word of words) {
    const padded = word.padEnd(maxLength, ' ');
    console.log(`* ${padded} *`);
  }
  console.log(border);

  rl.close();
});
