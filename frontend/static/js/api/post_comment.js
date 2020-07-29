const token = localStorage.getItem("token")
const form = document.querySelector('#post_comment_form');
const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value

if(token != null){
    document.querySelector("#name-group").remove();
}

const formEvent = form.addEventListener('submit', event => {
    event.preventDefault();
    const body = document.querySelector("#message").value
    const title = document.querySelector("#title").value
    let username = ""
    if(document.querySelector("#name") != null)
    {
        username = document.querySelector("#name").value
    }
    const post_id = parseInt(document.querySelector("#post-id").value)

    if (token != null){
        headers = {
            "Authorization" : `Token ${token}`
        }
    } else {
        headers = {}
    }
    axios.post(window.location.origin + '/api/comments/', {'title' : title, 'body' : body, 'username' : username, 'post' : post_id}, {headers : headers})
        .then(response => {
            window.location.reload();
        })
        // TODO print errors to the page rather than the console
        .catch(error => console.error(error));
});