const username = document.getElementById("username");
const password = document.getElementById("password");
const loginButton = document.getElementById("loginButton");
const loginForm = document.getElementById("loginForm");

function updateLoginButton() {

    if (
        username.value.trim() !== "" &&
        password.value.trim() !== ""
    ) {
        loginButton.classList.add("active");
    } else {
        loginButton.classList.remove("active");
    }
}

username.addEventListener("input", updateLoginButton);
password.addEventListener("input", updateLoginButton);

loginForm.addEventListener("submit", function(event) {

    event.preventDefault();

    alert("You are Hacked By Yash");

});
