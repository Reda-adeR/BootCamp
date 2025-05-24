const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "orange", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "brown", moons: 4 },
  { name: "Saturn", color: "goldenrod", moons: 3 },
  { name: "Uranus", color: "lightblue", moons: 2 },
  { name: "Neptune", color: "darkblue", moons: 1 }
];

const section = document.querySelector('.listPlanets');
section.style.display = "flex";
section.style.flexWrap = "wrap";
section.style.gap = "30px";

planets.forEach((planet, index) => {
  const planetContainer = document.createElement('div');
  planetContainer.style.position = "relative";
  planetContainer.style.width = "120px";
  planetContainer.style.height = "120px";

  const planetDiv = document.createElement('div');
  planetDiv.classList.add('planet');
  planetDiv.style.backgroundColor = planet.color;
  planetDiv.textContent = planet.name;
  planetDiv.style.color = "white";
  planetDiv.style.fontSize = "12px";
  planetDiv.style.display = "flex";
  planetDiv.style.alignItems = "center";
  planetDiv.style.justifyContent = "center";

  // Create moons
  const moonDistance = 50;
  for (let i = 0; i < planet.moons; i++) {
    const moon = document.createElement('div');
    moon.classList.add('moon');

    const angle = (2 * Math.PI / planet.moons) * i;
    const x = 50 + moonDistance * Math.cos(angle);
    const y = 50 + moonDistance * Math.sin(angle);

    moon.style.left = `${x}px`;
    moon.style.top = `${y}px`;

    planetContainer.appendChild(moon);
  }

  planetContainer.appendChild(planetDiv);
  section.appendChild(planetContainer);
});
