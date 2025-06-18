const resolveInFourSeconds = new Promise((resolve) => {
  setTimeout(() => {
    resolve("success");
  }, 4000);
});

resolveInFourSeconds.then(result => console.log(result));
