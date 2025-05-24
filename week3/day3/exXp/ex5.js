const div = document.getElementById("container");
console.log(div);

document.querySelectorAll(".list")[0].children[1].textContent = "Richard";
document.querySelectorAll(".list")[1].children[1].remove();

document.querySelectorAll(".list").forEach(ul => {
    ul.firstElementChild.textContent = "YourName";
    ul.classList.add("student_list");
});

document.querySelector(".list").classList.add("university", "attendance");

div.style.backgroundColor = "lightblue";
div.style.padding = "10px";

const liList = document.querySelectorAll("li");
liList.forEach(li => {
    if (li.textContent === "Dan") li.style.display = "none";
    if (li.textContent === "Richard") li.style.border = "1px solid black";
});

document.body.style.fontSize = "20px";

if (div.style.backgroundColor === "lightblue") {
    const names = Array.from(document.querySelectorAll("ul")[0].children).map(li => li.textContent);
    alert(`Hello ${names.join(" and ")}`);
}
