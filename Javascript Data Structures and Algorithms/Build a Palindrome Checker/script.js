function checkPalindrome() {
    // Get the input text, convert it to lowercase, and remove non-alphanumeric characters
    const inputText = document.getElementById('text-input').value.toLowerCase().replace(/[^a-z0-9]/g, '');

    // Get the result element where we will display the result
    const resultElement = document.getElementById('result');

    // Check if the input text is empty
    if (inputText === '') {
        // Display an alert if the input is empty
        alert('Please input a value');
    } else {
        // Reverse the input text to check for palindrome
        const reversedText = inputText.split('').reverse().join('');

        // Check if the input text is the same when reversed
        const isPalindrome = inputText === reversedText;

        // Display the original input text in the resultElement along with the palindrome check result
        if (isPalindrome) {
            resultElement.textContent = `${document.getElementById('text-input').value} is a palindrome`;
        } else {
            resultElement.textContent = `${document.getElementById('text-input').value} is not a palindrome`;
        }
    }
}
