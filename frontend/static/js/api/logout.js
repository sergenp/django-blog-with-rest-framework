if (token != null) {
    const logout_link = document.querySelector('#logout-link');
    logout_link.addEventListener('click', event => {
        event.preventDefault();
        axios.post('/api/auth/logout', {}, { headers: headers})
            .then(response => {
                localStorage.removeItem("token")
                window.location.replace("/")
            })
            // TODO print errors to the page rather than the console
            .catch(error => console.error(error));
    });
}