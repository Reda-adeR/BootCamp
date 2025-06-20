const morse = `{
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
  "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
  "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
  "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
  "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
  "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
  "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.",
  ")": "-.--.-"
}`;


function toJs() {
  return new Promise((resolve, reject) => {
    const morseJS = JSON.parse(morse);
    if (Object.keys(morseJS).length === 0) {
      reject("Error: Morse object is empty");
    } else {
      resolve(morseJS);
    }
  });
}

function toMorse(morseJS) {
  return new Promise((resolve, reject) => {
    const userInput = prompt("Enter a word or sentence").toLowerCase();
    const translation = [];

    for (let char of userInput) {
      if (morseJS[char]) {
        translation.push(morseJS[char]);
      } else {
        reject(`Error: Character "${char}" not in Morse data`);
        return;
      }
    }

    resolve(translation);
  });
}

function joinWords(morseTranslation) {
  const output = morseTranslation.join('\n');
  document.body.innerHTML = `<pre>${output}</pre>`;
}


toJs()
  .then(toMorse)
  .then(joinWords)
  .catch(error => console.log(error));
