const button = document.getElementById("getCharacter");
const loader = document.getElementById("loader");
const error = document.getElementById("error");
const card = document.getElementById("character");

const nameEl = document.getElementById("name");
const heightEl = document.getElementById("height");
const genderEl = document.getElementById("gender");
const birthYearEl = document.getElementById("birthYear");
const homeworldEl = document.getElementById("homeworld");

button.addEventListener("click", async () => {
  const randomId = Math.floor(Math.random() * 83) + 1;

  loader.classList.remove("hidden");
  error.classList.add("hidden");
  card.classList.add("hidden");

  try {
    const res = await fetch(`https://www.swapi.tech/api/people/${randomId}`);
    if (!res.ok) throw new Error("Network response was not ok.");
    const data = await res.json();

    const { name, height, gender, birth_year, homeworld } = data.result.properties;

    const homeRes = await fetch(homeworld);
    const homeData = await homeRes.json();
    const planetName = homeData.result.properties.name;

    nameEl.textContent = name;
    heightEl.textContent = height + " cm";
    genderEl.textContent = gender;
    birthYearEl.textContent = birth_year;
    homeworldEl.textContent = planetName;

    card.classList.remove("hidden");
  } catch (err) {
    error.textContent = "Failed to fetch character data. Please try again.";
    error.classList.remove("hidden");
  } finally {
    loader.classList.add("hidden");
  }
});
