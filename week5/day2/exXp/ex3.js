async function getStarship() {
  try {
    const response = await fetch("https://www.swapi.tech/api/starships/9/");
    if (!response.ok) throw new Error("Failed to fetch starship");
    const data = await response.json();
    console.log(data.result);
  } catch (error) {
    console.error("Error:", error);
  }
}

getStarship();
