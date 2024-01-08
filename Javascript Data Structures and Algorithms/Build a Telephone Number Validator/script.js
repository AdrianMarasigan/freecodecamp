// Add an event listener to the Check button
document.getElementById('check-btn').addEventListener('click', function () {
    validatePhoneNumber();
});

// Add an event listener to the Clear button
document.getElementById('clear-btn').addEventListener('click', function () {
    clearResults();
});

// Function to validate the phone number
function validatePhoneNumber() {
    // Get the user input and trim any leading/trailing whitespaces
    var userInput = document.getElementById('user-input').value.trim();
    // Get the div element where results will be displayed
    var resultsDiv = document.getElementById('results-div');

    // Check if the input is empty
    if (userInput === '') {
        // Show an alert if the input is empty
        alert('Please provide a phone number');
        return;
    }

    // Regular expression for valid US phone numbers
    var regex = /^(1\s?)?(\(\d{3}\)|\d{3})([\s\-]?)\d{3}([\s\-]?)\d{4}$/;

    // Test the input against the regex
    if (regex.test(userInput)) {
        // Display a valid message if the input matches the regex
        resultsDiv.textContent = 'Valid US number: ' + userInput;
    } else {
        // Display an invalid message if the input does not match the regex
        resultsDiv.textContent = 'Invalid US number: ' + userInput;
    }
}

// Function to clear the results
function clearResults() {
    // Clear the content within the results div
    document.getElementById('results-div').textContent = '';
}
