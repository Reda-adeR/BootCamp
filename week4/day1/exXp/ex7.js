// In your JS
(function(user) {
    const navbar = document.getElementById('navbar');
    navbar.innerHTML += `
        <div class="user-profile">
            <img src="profile.jpg" alt="${user}'s profile" width="50">
            <span>Welcome, ${user}!</span>
        </div>
    `;
})("John");