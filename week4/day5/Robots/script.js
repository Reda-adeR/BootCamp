// Robot data
const robots = [
    { name: "Leanne Graham", username: "Sincere@april.biz" },
    { name: "Ervin Howell", username: "Shanna@melissa.tv" },
    { name: "Clementine Bauch", username: "Nathan@yesenia.net" },
    { name: "Patricia Lebsack", username: "Julianne.OConner@kory.org" },
    { name: "Chelsey Dietrich", username: "Lucio_Hettinger@annie.ca" },
    { name: "Mrs. Dennis Schulist", username: "Karley_Dach@jasper.info" },
    { name: "Kurtis Weissnat", username: "Telly.Hoeger@billy.biz" },
    { name: "Nicholas Runolfsdottir V", username: "Sherwood@rosamond.me" },
    { name: "Glenna Reichert", username: "Chaim_McDermott@dana.io" },
    { name: "Clementina DuBuque", username: "Rey.Padberg@karina.biz" },
    { name: "Mohammed khibra", username: "M.diverg@korona.iz" },
    { name: "Abdellah robiot", username: "robiotor@merane.fe" },
    { name: "Picasso bot", username: "picasso@separe.ize" },
    { name: "Milano amar", username: "sarter@smart.co" },
    { name: "Cifer polo", username: "venome@pile.fr" },
    { name: "Helfer Proto", username: "M.diverg@korona.iz" },
    { name: "Yasser Moustaine", username: "yasser@mgail.moc" }
];

// Function to generate robot cards
function renderRobots(robotsArray) {
    const robotGrid = document.getElementById('robotGrid');
    robotGrid.innerHTML = '';
    
    robotsArray.forEach(robot => {

        const card = document.createElement('div');
        card.className = 'robotCard';
        card.title = robot.name
        
        const img = document.createElement('img');
        img.className = 'robotImage';
        img.src = `https://robohash.org/${robot.username}?size=200x200`;
        img.alt = robot.name;
        
        const name = document.createElement('h3');
        name.className = 'robotName';
        name.textContent = robot.name;
        
        const username = document.createElement('p');
        username.className = 'robotUsername';
        username.textContent = robot.username;
        
        card.appendChild(img);
        card.appendChild(name);
        card.appendChild(username);
        
        robotGrid.appendChild(card);
    });
}

// Search functionality
document.getElementById('searchBox').addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filteredRobots = robots.filter(robot => 
        robot.name.toLowerCase().includes(searchTerm) || 
        robot.username.toLowerCase().includes(searchTerm)
    );
    renderRobots(filteredRobots);
});

// Initial render
renderRobots(robots);