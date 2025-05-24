// Function to calculate average
function calculateAverage(gradesList) {
  let sum = 0;
  for (let i = 0; i < gradesList.length; i++) {
    sum += gradesList[i];
  }
  return sum / gradesList.length;
}

// Function to find average and evaluate result
function findAvg(gradesList) {
  let avg = calculateAverage(gradesList);
  console.log(`Average: ${avg}`);

  if (avg > 65) {
    console.log("Congratulations, you passed!");
  } else {
    console.log("You failed and must repeat the course.");
  }
}

// Example usage:
findAvg([70, 85, 60, 90, 45]);
