function userLogin() {

    const email = document.getElementById("login_email").value
    const password = document.getElementById("login_password").value

    $.ajax({
        type: "GET",
        url: "check",
        data: {
            "myvalue": email+","+password,
        },
        dataType: "json"
    }).done(function (json) {
        $.each(json, function (key, val) {
            if (val === "Success") {
                alert("Login Successful, directing you to home page");
                document.location.href = "../home/Home.html"
            } else{
                alert("Error: " + val);
            }
        });
    });
}

