function userRegister() {

    const email = document.getElementById("register_email").value
    const password = document.getElementById("register_password").value

    $.ajax({
        type: "GET",
        url: "check",
        data: {
            "myvalue": email.concat(",", password),
        },
        dataType: "json"
    }).done(function (json) {
        $.each(json, function (key, val) {
            if (val === "Success") {
                alert("Registration Successful, directing you to home page");
                document.location.href = "../home/Home.html"
            }
        });
    });
}