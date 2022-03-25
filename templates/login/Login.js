// document.getElementById(id_name)
// document.getElementsByClassName('class_name')
// document.querySelector('selector')


// const loginForm = document.getElementById("login-form");
// const loginButton = document.getElementById("login-form-submit");
// const loginErrorMsg = document.getElementById("login-error-msg");
//
// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const username = loginForm.username.value;
//     const password = loginForm.password.value;
//
//     if (username === "user" && password === "web_dev") {
//         alert("You have successfully logged in.");
//         location.reload();
//     } else {
//         loginErrorMsg.style.opacity = 1;
//     }
// })


function myFunction(){
    const email = document.getElementById("login_email").value
    const password = document.getElementById("login_password").value

    if(email==="test@abc.com" && password==="123123"){
        alert("Success, directing you to home page");
        document.location.href = "../home/Home.html"
    }else{
        alert("Invalid credentials");
    }

}