const form = document.getElementById("gifForm");
const input = document.getElementById("searchInput");
const gifResults = document.getElementById("gifResults");
const deleteAllBtn = document.getElementById("deleteAll");

const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const category = input.value.trim();
  if (!category) return;

  const url = `https://api.giphy.com/v1/gifs/random?tag=${category}&api_key=${API_KEY}`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to fetch gif");

    const data = await response.json();
    const gifUrl = data.data.images.original.url;

    const container = document.createElement("div");
    container.classList.add("gif-container");

    const img = document.createElement("img");
    img.src = gifUrl;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "DELETE";
    deleteBtn.onclick = () => container.remove();

    container.appendChild(img);
    container.appendChild(deleteBtn);
    gifResults.appendChild(container);
  } catch (error) {
    console.error("Error:", error);
    alert("Could not fetch GIF.");
  }

  input.value = "";
});

deleteAllBtn.addEventListener("click", () => {
  gifResults.innerHTML = "";
});
