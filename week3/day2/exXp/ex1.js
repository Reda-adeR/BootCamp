// 🌟 Exercise 1 : List of people
const people = ["Greg", "Mary", "Devon", "James"];

// Remove “Greg”
people.shift();

// Replace “James” with “Jason”
people[people.indexOf("James")] = "Jason";

// Add your name
people.push("YourName");

// Log Mary’s index
console.log(people.indexOf("Mary"));

// Copy array without Mary and your name
const newPeople = people.slice(1, 3);
console.log(newPeople);

// Index of Foo
console.log(people.indexOf("Foo")); // -1 because Foo is not in the array

// Last element
const last = people[people.length - 1];
console.log(last);

// Part II - Loops
for (let person of people) {
  console.log(person);
}

for (let person of people) {
  console.log(person);
  if (person === "Devon") break;
}

