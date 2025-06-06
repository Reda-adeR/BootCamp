let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
};

// Part 1: Display fruits
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};
displayGroceries();
// Output:
// pear
// apple
// banana

// Part 2: Clone and test references
const cloneGroceries = () => {
    // Copying primitive value (string)
    let user = client;
    console.log(`Original client: ${client}, User: ${user}`); // Both "John"
    
    client = "Betty";
    console.log(`After change - Client: ${client}, User: ${user}`);
    // Client: "Betty", User: "John" (user didn't change because strings are primitive values)
    
    // Copying object reference
    let shopping = groceries;
    console.log(`Original totalPrice: ${shopping.totalPrice}`); // "20$"
    
    shopping.totalPrice = "35$";
    console.log(`Modified totalPrice: ${groceries.totalPrice}`); // "35$"
    // Both changed because objects are passed by reference
    
    shopping.other.paid = false;
    console.log(`Modified paid status: ${groceries.other.paid}`); // false
    // Both changed because nested objects are still references
};

cloneGroceries();