function userRegister() {

    const name = document.getElementById("register_name").value
    const phone = document.getElementById("register_phone").value
    const address = document.getElementById("register_address").value
    const email = document.getElementById("register_email").value
    const balance = document.getElementById("register_balance").value
    const password = document.getElementById("register_password").value

    $.ajax({
        type: "GET",
        url: "check",
        data: {
            "myvalue": name + "," + phone + "," + address + "," + email + "," + balance + "," + password,
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