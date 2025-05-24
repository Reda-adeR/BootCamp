function changeEnough(itemPrice, amountOfChange) {
    const total = amountOfChange[0]*0.25 + amountOfChange[1]*0.10 + amountOfChange[2]*0.05 + amountOfChange[3]*0.01;
    return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
console.log(changeEnough(14.11, [2,100,0,0]));   // false
console.log(changeEnough(0.75, [0,0,20,5]));     // true
