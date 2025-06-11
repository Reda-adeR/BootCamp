const users = { user1: 18273, user2: 92833, user3: 90315 };

// ---------1
const usersArray = Object.entries(users);
console.log(usersArray);

// --------2
const updatedUsersArray = usersArray.map(([key, value]) => [key, value * 2]);
console.log(updatedUsersArray);
