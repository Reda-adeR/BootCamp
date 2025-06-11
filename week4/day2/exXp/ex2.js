const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

colors.forEach((color, index) => {
  let suffix = ordinal[(index + 1)] || "th";
  if (index + 1 > 3) suffix = "th";
  console.log(`${index + 1}${suffix} choice is ${color}.`);
});
