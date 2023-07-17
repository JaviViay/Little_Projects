// allowed characters
const lowercaseChars = 'abcdefghijklmnñopqrstuvwxyz';
const uppercaseChars = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';
const numericChars = '0123456789';
const specialChars = '!@#$%^&*()_-+=<>?';

// connect to the button and the output
const generateBtn = document.getElementById('generate');
const outputField = document.getElementById('output');

// function to generate the passwd
function generatePassword() {
  let password = '';
  // combine the characters
  const allowedChars = lowercaseChars + uppercaseChars + numericChars + specialChars;
  // generate passwd
  for (let i = 0; i < 12; i++) {
    const randomIndex = Math.floor(Math.random() * allowedChars.length);
    password += allowedChars[randomIndex];
  }
  // show the new passwd
  outputField.value = password;
}

// button action
generateBtn.addEventListener('click', generatePassword);