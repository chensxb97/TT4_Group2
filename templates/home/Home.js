function addRowToCurrentLoans() {
          
    var description = document.getElementById("description");
    var balance = document.getElementById("balance");
    var paid = 0
    var table = document.getElementById("myCurrentLoans");
    var lastRow = table.rows.length;

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = lastRow?lastRow:0
    row.insertCell(1).innerHTML= description.value;
    row.insertCell(2).innerHTML= balance.value;
    row.insertCell(3).innerHTML = 0
}
 
function updateCurrentLoans(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myCurrentLoans");
    var serial = document.getElementById("serial");
    var payment = document.getElementById("payment");
}

function addRowToLoanHistory() {
          
    var description = document.getElementById("description");
    var amount = document.getElementById("amount");
    var table = document.getElementById("myCurrentLoans");
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML = 'New';
    row.insertCell(1).innerHTML= description.value;
    row.insertCell(2).innerHTML= amount.value;
    row.insertCell(3).innerHTML = amount.value
 
}

function updateCurrentLoans(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myCurrentLoans");
    table.deleteRow(index);
    
}

 
function load() {
    
    console.log("Page load finished");
 
}