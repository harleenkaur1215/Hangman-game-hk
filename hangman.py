import random
import time

HANGMAN_PICS = [
    '''
    +---+
         |
         |
         |
        ===
    ''',
    '''
    +---+
    O   |
        |
        |
       ===
    ''',
    '''
    +---+
    O   |
    |   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|   |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
        |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
   /    |
       ===
    ''',
    '''
    +---+
    O   |
   /|\  |
   / \  |
       ===
    '''
]

words_by_category = {
    'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    'fruits': 'apple banana cherry date elderberry fig grapefruit guava honeydew kiwi lemon mango nectarine orange peach pear quince raspberry strawberry tangerine'.split(),
    'countries': 'afghanistan albania algeria andorra angola antigua argentina armenia australia austria azerbaijan bahamas bahrain bangladesh barbados belarus belgium belize benin bhutan bolivia bosnia botswana brazil brunei bulgaria burkina faso burundi cambodia cameroon canada cape verde chad chile china colombia comoros congo costa rica croatia cuba cyprus czech republic denmark djibouti dominica ecuador egypt el salvador equatorial guinea eritrea estonia ethiopia fiji finland france gabon gambia georgia germany ghana greece grenada guatemala guinea guinea-bissau guyana haiti honduras hungary iceland india indonesia iran iraq ireland israel italy jamaica japan jordan kazakhstan kenya kiribati kosovo kuwait kyrgyzstan laos latvia lebanon lesotho liberia libya liechtenstein lithuania luxembourg macedonia madagascar malawi malaysia maldives mali malta marshall islands mauritania mauritius mexico micronesia moldova monaco mongolia montenegro morocco mozambique myanmar namibia nauru nepal netherlands new zealand nicaragua niger nigeria north korea norway oman pakistan palau panama papua paraguay peru philippines poland portugal qatar romania russia rwanda samoa san marino sao tome saudi arabia senegal serbia seychelles sierra leone singapore slovakia slovenia solomon islands somalia south africa south korea south sudan spain sri lanka sudan suriname swaziland sweden switzerland syria taiwan tajikistan tanzania thailand timor-leste togo tonga trinidad tunisia turkey turkmenistan tuvalu uganda ukraine united arab emirates united kingdom united states uruguay uzbekistan vanuatu vatican city venezuela vietnam yemen zambia zimbabwe'.split(),
    'colors': 'red green blue yellow orange white black purple gray lime maroon navy brown coral cyan magenta indigo turquoise gold silver ivory beige'.split(),
    'flowers': 'rose tulip daisy lily lotus orchid bolossom iris poppy sunflower daffodil dandelion petunia bluebell hyacinth lavender'.split(),
    'indian states': 'jammukashmir himachal uttarakhand punjab haryana uttarpradesh assam tamilnadu kerela maharashtra goa bihar chattisgarh ladakh rajasthan gujrat madhyapradesh karnatka odisha jharkhand westbengal arunachalpraesh nagaland mizoram manipur tripura meghalya sikkim telangana'.split(),
    'programming languages': 'python javascript java c cp php sql swift rust nextjs tablue ruby kotlin typescript pearl golang django html css react'.split(),
    'languages': 'hindi punjabi english dogri urdu french spanish assamase bengali bodo gujrati kannada kashmiri monkani maithili malayalam marathi meitei nepali odia sanskrit sindhi tamil telugu santali portuguese dari arabic german russian dutch bulgarian greek korean danish indonesian thai turkish chinese'.split(),
    'shapes': 'circle sqaure rectangle trapezium cuboid cube pyramid sphere ring disc pentagon heart star hexagon crescent cylinder'.split(),
    'luxury brands': 'gucci prada dior lv versace armani rolex balmani tiffany fendi chanel burberry hermes calvinklien boss chloe michaelkors jimmychoo givenchy kenzo nike'.split(),
}

def getRandomWord(wordList):
    """
    Returns a random string from the passed list of strings.
    """
    return random.choice(wordList)

def displayBoard(missedLetters, correctLetters, secretWord):
    """
    Displays the hangman board with missed letters, correct letters, and the secret word's current state.
    """
    print()
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', ' '.join(missedLetters))
    blanks = ''.join(letter if letter in correctLetters else '_' for letter in secretWord)
    print('Current word:', ' '.join(blanks))
    print()

def getGuess(alreadyGuessed):
    """
    Prompts the player to enter a guess.
    """
    while True:
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter.')
        else:
            return guess

def selectCategory():
    """
    Prompts the user to select a category and returns the selected category.
    """
    print('Select a category:')
    for idx, category in enumerate(words_by_category.keys(), 1):
        print(f'{idx}. {category.capitalize()}')
    while True:
        try:
            choice = int(input())
            if 1 <= choice <= len(words_by_category):
                return list(words_by_category.keys())[choice - 1]
            else:
                print('Invalid choice. Please select a number from the list.')
       
