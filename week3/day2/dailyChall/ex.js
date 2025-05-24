function cleanSentence(sentence) {
  let wordNot = sentence.indexOf("not");
  let wordBad = sentence.indexOf("bad");

  if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    return sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  } else {
    return sentence;
  }
}

// Test cases
console.log(cleanSentence("The movie is not that bad, I like it"));

console.log(cleanSentence("This dinner is not that bad ! You cook well"));

console.log(cleanSentence("This movie is not so bad !"));

console.log(cleanSentence("This dinner is bad !"));

console.log(cleanSentence("That wasn't bad at all"));

console.log(cleanSentence("The weather is not great"));
