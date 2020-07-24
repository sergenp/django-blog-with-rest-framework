if (localStorage.getItem("token") != null){
    window.location.replace("/");
}

const form = document.querySelector('form');
const formEvent = form.addEventListener('submit', event => {
    event.preventDefault();
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;
    axios.post('/api/auth/login', { username, password })
        .then(response => {
            localStorage.setItem("token", response.data.token)
            window.location.replace("/");
        })
        // TODO print errors to the page rather than the console
        .catch(error => console.error(error));
});