


// Get the reference to the input element
var inputElement = document.getElementById("date");
// var inputElement = document.getElementById("edate");

// Get the current date
var currentDate = new Date();

// Format the date as "yyyy-mm-dd"
var formattedDate = currentDate.toISOString().split('T')[0];

// Set the value of the input element to the formatted date
inputElement.value = formattedDate;
