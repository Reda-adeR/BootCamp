(function(children, partner, location, job) {
    const fortune = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
    document.body.innerHTML += `<p>${fortune}</p>`;
})(2, "Alex", "Paris", "web developer");