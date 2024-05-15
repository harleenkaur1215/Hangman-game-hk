const wordElement = document.getElementById('word');
const wrongLettersElement = document.getElementById('wrong-letters');
const playButton = document.getElementById('play-button');
const popupContainer = document.getElementById('popup-container');
const notificationContainer = document.getElementById('notification-container');
const finalMessageElement = document.getElementById('final-message');

const hangmanParts = document.querySelectorAll('.figure-part');

const wordsList = ['application', 'programming', 'interface', 'wizard'];
let randomWord = wordsList[Math.floor(Math.random() * wordsList.length)];

let correctGuesses = [];
let incorrectGuesses = [];

// Display the current word
function updateWordDisplay() {
    wordElement.innerHTML = `
        ${randomWord.split('')
        .map(letter => `
            <span class="letter">
                ${correctGuesses.includes(letter) ? letter : ''}
            </span>
        `)
        .join('')}
    `;

    const currentWord = wordElement.innerText.replace(/\n/g, '');

    if (currentWord === randomWord) {
        finalMessageElement.textContent = 'Congratulations! You won! 😃';
        popupContainer.style.display = 'flex';
    }
}

// Update the wrong letters
function updateIncorrectGuesses() {
    wrongLettersElement.innerHTML = `
        ${incorrectGuesses.length > 0 ? '<p>Wrong</p>' : ''}
        ${incorrectGuesses.map(letter => `<span>${letter}</span>`).join('')}
    `;

    hangmanParts.forEach((part, index) => {
        const errorCount = incorrectGuesses.length;
        part.style.display = index < errorCount ? 'block' : 'none';
    });

    if (incorrectGuesses.length === hangmanParts.length) {
        finalMessageElement.textContent = 'Unfortunately you lost. 😕';
        popupContainer.style.display = 'flex';
    }
}

// Show notification
function showAlert() {
    notificationContainer.classList.add('show');
    setTimeout(() => {
        notificationContainer.classList.remove('show');
    }, 2000);
}

// Handle keypress events
window.addEventListener('keydown', event => {
    if (event.keyCode >= 65 && event.keyCode <= 90) {
        const key = event.key.toLowerCase();
        if (randomWord.includes(key)) {
            if (!correctGuesses.includes(key)) {
                correctGuesses.push(key);
                updateWordDisplay();
            } else {
                showAlert();
            }
        } else {
            if (!incorrectGuesses.includes(key)) {
                incorrectGuesses.push(key);
                updateIncorrectGuesses();
            } else {
                showAlert();
            }
        }
    }
});

// Restart the game
playButton.addEventListener('click', () => {
    correctGuesses = [];
    incorrectGuesses = [];
    randomWord = wordsList[Math.floor(Math.random() * wordsList.length)];

    updateWordDisplay();
    updateIncorrectGuesses();

    popupContainer.style.display = 'none';
});

updateWordDisplay();
