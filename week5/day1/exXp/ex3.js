const promiseResolved = Promise.resolve(3);
promiseResolved.then(value => console.log(value));

const promiseRejected = Promise.reject("Boo!");
promiseRejected.catch(error => console.log(error));