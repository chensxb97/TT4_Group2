function addRowToCurrentLoans() {
          
    var description = document.getElementById("description");
    var dt = Date()
    var balance = document.getElementById("balance");
    var table = document.getElementById("myCurrentLoans");
    var lastRow = table.rows.length;

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = lastRow?lastRow:0
    row.insertCell(1).innerHTML = dt
    row.insertCell(2).innerHTML= description.value;
    row.insertCell(3).innerHTML= balance.value;
}
 
function updateCurrentLoans() {

    var table = document.getElementById("myCurrentLoans");
    var serial = document.getElementById("serial");
    var payment = document.getElementById("payment");

    // Obtain old values by serial no

    // GET THE CELLS COLLECTION OF THE CURRENT ROW.
    var objCells = table.rows.item(serial.value).cells;
    var curBalance = objCells.item(3).innerHTML;

    console.log(curBalance)

    // // Update
    table.rows[serial.value].cells[3].innerHTML = curBalance - payment.value;

    // Delete any rows with curBalance
    
}

function addRowToLoanHistory() {
          
    var description = document.getElementById("description");
    var dt = Date()
    var balance = document.getElementById("balance");
    var table = document.getElementById("myLoanHistory");
    var lastRow = table.rows.length;

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = lastRow?lastRow:0
    row.insertCell(1).innerHTML = dt
    row.insertCell(2).innerHTML= description.value;
    row.insertCell(3).innerHTML= balance.value;
    row.insertCell(4).innerHTML = 'Pending'
}

 
function load() {
    
    console.log("Page load finished");
 
}