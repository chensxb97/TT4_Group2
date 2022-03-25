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