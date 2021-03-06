function addRowToCurrentLoans() {
          
    var dt = Date()
    var balance = document.getElementById("balance").value;
    var table = document.getElementById("myCurrentLoans");
    var lastRow = table.rows.length;

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = lastRow?lastRow:0
    row.insertCell(1).innerHTML = dt
    row.insertCell(2).innerHTML= '-';
    row.insertCell(3).innerHTML= balance;

    $.ajax({
        type: "POST",
        url: "check",
        data: {
            "myvalue": balance,
        },
        dataType: "json"
    }).done(function (json) {
        $.each(json, function (key, val) {
            if (val === "Success") {
                alert("POST Successful");
            }
        });
    });
}

function updateCurrentLoans() {

    var table = document.getElementById("myCurrentLoans");
    var serial = document.getElementById("serial");
    var payment = document.getElementById("payment");

    // Obtain old values by serial no
    var objCells = table.rows.item(serial.value).cells;
    var curBalance = objCells.item(3).innerHTML;

    console.log(curBalance)
    var newBalance = curBalance - payment.value;

    // Update balance
    table.rows[serial.value].cells[3].innerHTML = newBalance;

    $.ajax({
        type: "PATCH",
        url: "check",
        data: {
            "myvalue": newBalance,
        },
        dataType: "json"
    }).done(function (json) {
        $.each(json, function (key, val) {
            if (val === "Success") {
                alert("PATCH Successful");
            }
        });
    });
    
    // Delete loan from frontend if it has negative curBalance + Update Loan History
    console.log(parseInt(table.rows.item(serial.value).cells[3].innerText, 10))
    if (parseInt(table.rows.item(serial.value).cells[3].innerText, 10) <= 0){
        document.getElementById('myCurrentLoans').deleteRow(serial.value);
        var loanTable = document.getElementById('myLoanHistory');
        loanTable.rows[serial.value].cells[4].innerHTML = 'Completed';
    };
}

function addRowToLoanHistory() {
    var dt = Date();
    var balance = document.getElementById("balance").value;
    var table = document.getElementById("myLoanHistory");
    var lastRow = table.rows.length;

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = lastRow?lastRow:0;
    row.insertCell(1).innerHTML = dt;
    row.insertCell(2).innerHTML= '-';
    row.insertCell(3).innerHTML= balance;
    row.insertCell(4).innerHTML = 'Pending';
}

function load() {
    console.log("Page load finished");
}
