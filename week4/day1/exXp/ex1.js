// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`); // Prediction: "inside the funcOne function 3"
}

// #1.1 - Output: "inside the funcOne function 3" (a is reassigned to 3)
// #1.2 - With const: Error (can't reassign const variable)

// #2
let a = 0;
function funcTwo() {
    a = 5; // Modifies the global a
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - Console sequence:
// funcThree() → "inside the funcThree function 0" (global a is 0)
// funcTwo() → changes global a to 5
// funcThree() → "inside the funcThree function 5" (global a was modified)
// #2.2 - With const: Error (can't reassign const variable)

// #3
function funcFour() {
    window.a = "hello"; // Sets global a property on window
}

function funcFive() {
    alert(`inside the funcFive function ${a}`); // Accesses window.a
}

// #3.1 - Console sequence:
// funcFour() → sets window.a
// funcFive() → "inside the funcFive function hello"

// #4
let a = 1;
function funcSix() {
    let a = "test"; // Local scope a shadows global a
    alert(`inside the funcSix function ${a}`);
}

// #4.1 - Output: "inside the funcSix function test" (local a used)
// #4.2 - With const: Same behavior (const works like let in this case)

// #5
let a = 2;
if (true) {
    let a = 5; // Block-scoped a
    alert(`in the if block ${a}`); // Output: "in the if block 5"
}
alert(`outside of the if block ${a}`); // Output: "outside of the if block 2" (original a)

// #5.1 - Output sequence: "in the if block 5" then "outside of the if block 2"
// #5.2 - With const: Same behavior (const works like let in block scope)