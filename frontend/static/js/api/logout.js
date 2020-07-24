const logout_link = document.querySelector('#logout-link');

logout_link.addEventListener('click', event => {
    event.preventDefault();
    const token = localStorage.getItem("token");
    axios.post('/api/auth/logout', {}, { headers: { Authorization: "Token" + " " + token}})
        .then(response => {
            localStorage.removeItem("token")
            window.location.replace("/")
        })
        // TODO print errors to the page rather than the console
        .catch(error => console.error(error));
});