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

function updateWord() {
    wordElement.innerHTML = randomWord
        .split('')
        .map(letter => `<span class="letter">${correctGuesses.includes(letter) ? letter : ''}</span>`)
        .join('');

    const currentWord = wordElement.innerText.replace(/\n/g, '');

    if (currentWord === randomWord) {
        finalMessageElement.textContent = 'Congratulations! You won! 😃';
        popupContainer.style.display = 'flex';
    }
}

function updateWrongLetters() {
    wrongLettersElement.innerHTML = `${incorrectGuesses.length > 0 ? '<p>Wrong</p>' : ''}${incorrectGuesses.map(letter => `<span>${letter}</span>`).join('')}`;

    hangmanParts.forEach((part, index) => {
        part.style.display = index < incorrectGuesses.length ? 'block' : 'none';
    });

    if (incorrectGuesses.length === hangmanParts.length) {
        finalMessageElement.textContent = 'Unfortunately you lost. 😕';
        popupContainer.style.display = 'flex';
    }
}

function showNotification() {
    notificationContainer.classList.add('show');
    setTimeout(() => notificationContainer.classList.remove('show'), 2000);
}

window.addEventListener('keydown', event => {
    if (event.keyCode >= 65 && event.keyCode <= 90) {
        const letter = event.key.toLowerCase();
        if (randomWord.includes(letter)) {
            if (!correctGuesses.includes(letter)) {
                correctGuesses.push(letter);
                updateWord();
            } else {
                showNotification();
            }
        } else {
            if (!incorrectGuesses.includes(letter)) {
                incorrectGuesses.push(letter);
                updateWrongLetters();
            } else {
                showNotification();
            }
        }
    }
});

playButton.addEventListener('click', () => {
    correctGuesses = [];
    incorrectGuesses = [];
    randomWord = wordsList[Math.floor(Math.random() * wordsList.length)];
    updateWord();
    updateWrongLetters();
    popupContainer.style.display = 'none';
});

updateWord();
