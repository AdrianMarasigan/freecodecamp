// Add an event listener to the button to trigger the conversion when clicked
document.getElementById('convert-btn').addEventListener('click', convertToRoman);

// Function to convert the entered number to Roman numerals
function convertToRoman() {
    // Get the input value from the number input field
    const inputNumber = document.getElementById('number').value;

    // Get the output element where the result will be displayed
    const outputElement = document.getElementById('output');

    // Check if the input is empty or not a valid number
    if (inputNumber === '' || isNaN(inputNumber)) {
        outputElement.textContent = 'Please enter a valid number';
        return;
    }

    // Convert the input to an integer
    let num = parseInt(inputNumber);

    // Check if the number is within the valid range
    if (num < 1) {
        outputElement.textContent = 'Please enter a number greater than or equal to 1';
        return;
    }

    else if (num > 3999) {
        outputElement.textContent = 'Please enter a number less than or equal to 3999';
        return;
    }

    // Array of Roman numeral symbols
    const romanNumerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];

    // Corresponding values for each Roman numeral symbol
    const numeralValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    let result = '';

    // Convert the number to Roman numerals
    for (let i = 0; i < romanNumerals.length; i++) {
        while (num >= numeralValues[i]) {
            result += romanNumerals[i];
            num -= numeralValues[i];
        }
    }

    // Display the result in the output element
    outputElement.textContent = result;
    return
}
