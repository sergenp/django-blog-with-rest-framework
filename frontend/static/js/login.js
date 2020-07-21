if (localStorage.getItem("token") != null){
    window.location.replace("/");
}

const form = document.querySelector('form');

const formEvent = form.addEventListener('submit', event => {
    event.preventDefault();
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;
    const user = { username, password };
    loginUser(user);
});

const loginUser = (user) => {
    axios.post('/api/auth/login', user)
        .then(response => {
            response.data;
            localStorage.setItem("token", response.data.token)
            window.location.replace("/");
        })
        .catch(error => console.error(error));
};

