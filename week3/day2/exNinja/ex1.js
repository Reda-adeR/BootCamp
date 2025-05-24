// Person Objects with BMI method
let person1 = {
  fullName: "Alice Smith",
  mass: 68,
  height: 1.65,
  calculateBMI: function () {
    return this.mass / (this.height ** 2);
  }
};

let person2 = {
  fullName: "Bob Johnson",
  mass: 85,
  height: 1.75,
  calculateBMI: function () {
    return this.mass / (this.height ** 2);
  }
};

// Function to compare BMI
function compareBMI(p1, p2) {
  let bmi1 = p1.calculateBMI();
  let bmi2 = p2.calculateBMI();

  if (bmi1 > bmi2) {
    console.log(`${p1.fullName} has the highest BMI: ${bmi1.toFixed(2)}`);
  } else if (bmi2 > bmi1) {
    console.log(`${p2.fullName} has the highest BMI: ${bmi2.toFixed(2)}`);
  } else {
    console.log(`Both have the same BMI: ${bmi1.toFixed(2)}`);
  }
}

compareBMI(person1, person2);
