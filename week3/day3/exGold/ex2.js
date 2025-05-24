function abbrevName(name) {
  const [first, last] = name.split(' ');
  return `${first} ${last[0]}.`;
}

console.log(abbrevName("Robin Singh"));
