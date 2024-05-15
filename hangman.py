import random
import time

HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words_by_category = {
    'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    'fruits': 'apple banana cherry date elderberry fig grapefruit guava honeydew kiwi lemon mango nectarine orange peach pear quince raspberry strawberry tangerine'.split(),
    'countries': 'afghanistan albania algeria andorra angola antigua argentina armenia australia austria azerbaijan bahamas bahrain bangladesh barbados belarus belgium belize benin bhutan bolivia bosnia botswana brazil brunei bulgaria burkina faso burundi cambodia cameroon canada cape verde chad chile china colombia comoros congo costa rica croatia cuba cyprus czech republic denmark djibouti dominica ecuador egypt el salvador equatorial guinea eritrea estonia ethiopia fiji finland france gabon gambia georgia germany ghana greece grenada guatemala guinea guinea-bissau guyana haiti honduras hungary iceland india indonesia iran iraq ireland israel italy jamaica japan jordan kazakhstan kenya kiribati kosovo kuwait kyrgyzstan laos latvia lebanon lesotho liberia libya liechtenstein lithuania luxembourg macedonia madagascar malawi malaysia maldives mali malta marshall islands mauritania mauritius mexico micronesia moldova monaco mongolia montenegro morocco mozambique myanmar namibia nauru nepal netherlands new zealand nicaragua niger nigeria north korea norway oman pakistan palau panama papua paraguay peru philippines poland portugal qatar romania russia rwanda samoa san marino sao tome saudi arabia senegal serbia seychelles sierra leone singapore slovakia slovenia solomon islands somalia south africa south korea south sudan spain sri lanka sudan suriname swaziland sweden switzerland syria taiwan tajikistan tanzania thailand timor-leste togo tonga trinidad tunisia turkey turkmenistan tuvalu uganda ukraine united arab emirates united kingdom united states uruguay uzbekistan vanuatu vatican city venezuela vietnam yemen zambia zimbabwe'.split(),
 'colors ':'red green blue yellow orange white black purple gray lime maroon navy brown coral cyan magenta indigo turquoise gold silver ivory beige'.split(),
    'flowers ':'rose tulip daisy lily lotus orchid bolossom iris poppy sunflower daffodil dandelion petunia bluebell hyacinth lavender '.split(),
    'indian states ':'jammukashmir himachal uttarakhand punjab haryana uttarpradesh assam tamilnadu kerela maharashtra goa bihar chattisgarh ladakh rajasthan gujrat madhyapradesh karnatka odisha jharkhand westbengal arunachalpraesh nagaland mizoram manipur tripura meghalya sikkim telangana '.split(),
    'programming languages ':'python javascript java c cp php sql swift rust nextjs tablue ruby kotlin typescript pearl golang django html css react '.split(),
    'languages ':'hindi punjabi english dogri urdu french spanish assamase bengali bodo gujrati kannada kashmiri monkani maithili malayalam marathi meitei nepali odia sanskrit sindhi tamil telugu santali portuguese dari arabic german russian dutch bulgarian greek korean danish indonesian thai turkish chinese'.split(),
    'shapes ':'circle sqaure rectangle trapezium cuboid cube pyramid sphere ring disc pentagon heart star hexagon crescent cylinder '.split(),
    'luxury brands ': 'gucci prada dior lv versace armani rolex balmani tiffany fendi chanel burberry hermes calvinklien boss chloe michaelkors jimmychoo givenchy kenzo nike '.split(),

}

def getRandomWord(wordList):
    """
    Returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICS[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()

def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def selectCategory():
    """
    Prompts the user to select a category."""
    print('Select a category:')
    for idx, category in enumerate(words_by_category.keys()):
        print(f"{idx + 1}. {category.capitalize()}")
    while True:
        try:
            choice = int(input())
            if 1 <= choice <= len(words_by_category):
                return list(words_by_category.keys())[choice - 1]
            else:
                print('Invalid choice. Please select a number from the list.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def playAgain():
    """
    Returns True if the player wants to play again, False otherwise.
    """
    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')

def getRemainingTime(startTime, timeout):
    """
    Calculate the remaining time.
    """
    elapsed = time.time() - startTime
    remaining = max(0, timeout - elapsed)
    return remaining

print('|H_A_N_G_M_A_N|')

timeout = 120  # 5 sec timeout for each guess

while True:
    startTime = time.time()  # Start timer for guess
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False
    category = selectCategory()
    secretWord = getRandomWord(words_by_category[category])

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        remainingTime = getRemainingTime(startTime, timeout)
        print(f'Remaining time for guess: {round(remainingTime, 1)} seconds')
        
        if remainingTime <= 0:
            print("Time's up! You ran out of time for this guess.")
            if playAgain():
                break
            else:
                quit()
            break
        
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('You guessed it!')
                print('The secret word is "' + secretWord + '"! You win!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '".')
                gameIsDone = True
                if playAgain():
                    break
                else:
                    quit()

        if gameIsDone:
            if playAgain():
                break
            else:
                quit()
