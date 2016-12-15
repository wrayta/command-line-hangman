import random

"""-----------------------------------------------------------------"""
def setupGlobals():   

    global TRIES
    TRIES = 6 #how many tries the player gets to guess the word

    global DICT_WORD
    DICT_WORD = list(random.choice(LINES)) #select random word ALSO needed for 'game over' 

    global GUESSED_WORD
    GUESSED_WORD = []
    for i in range(0, len(DICT_WORD)):
        GUESSED_WORD.append('*') #word the player sees

    global GUESSES_LIST
    GUESSES_LIST = [] #the incorrect guesses

    global NUM_OF_BAD_GUESSES
    NUM_OF_BAD_GUESSES = 0 #counter for num of incorrect guesses
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def loadWords():

    global LINES #a list of all the possible hangman words

    LINES = open("Master_Word_List.txt").readlines()

    LINES = [word.lower().rstrip("\n") for word in LINES]
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def main():
    
    loadWords() #only do this once at application's start

    play = True
    while play:

        clearScreen()

        print("Hello, and welcome to 'Python Hangman'!")
        input("Press ENTER to continue...")

        clearScreen()

        setupGlobals()

        print("A random word has been selected...")
        input("Press ENTER to continue...")
        
        global NUM_OF_BAD_GUESSES

        while True: 

            clearScreen()
            printGuessedWord()
            printWrongGuesses()
            printHangman()

            letter = input("\nplease guess a letter: ")
            
            if not checkLetter(letter):
                addToGuessesList(letter)
                NUM_OF_BAD_GUESSES += 1 

            if GUESSED_WORD == DICT_WORD:
                clearScreen()
                printGuessedWord()
                printWrongGuesses()
                printHangman()
                play = doGameWon()
                break   
            elif NUM_OF_BAD_GUESSES == TRIES:
                clearScreen()
                printGuessedWord()
                printWrongGuesses()
                printHangman()
                play = doGameOver()       
                break     

"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def doGameWon():

    print("\nCONGRATULATIONS! YOU WON!!!")
    print("You correctly guessed " + ''.join(GUESSED_WORD))
    play = doPlayAgain()
    return play
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def doGameOver():

    print("\nGame Over. The word was " + ''.join(DICT_WORD))
    play = doPlayAgain()
    return play
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def doPlayAgain():

    play = True

    choice = input("Play again? Y/N... ")
    if choice == "n" or choice == "N":
        play = False
        input("Goodbye!")
    
    return play
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def printWrongGuesses():

    print(''.join(GUESSES_LIST) + "\n")
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def printGuessedWord():

    print(''.join(GUESSED_WORD), end="                    ")
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def printHangman():
    board = [[[], [], []],
           [[], [], []],
           [[], [], []]]

    if NUM_OF_BAD_GUESSES > 0:
        board[0][1] = '0'

    if NUM_OF_BAD_GUESSES > 1:
        board[1][1] = '|'

    if NUM_OF_BAD_GUESSES > 2:
        board[2][0] = '/'

    if NUM_OF_BAD_GUESSES > 3:
        board[2][2] = '\\'

    if NUM_OF_BAD_GUESSES > 4:
        board[1][0] = '-'

    if NUM_OF_BAD_GUESSES > 5:
        board[1][2] = '-'

    for cell in board:
        print(cell)
    
"""-----------------------------------------------------------------"""
    
"""-----------------------------------------------------------------"""  
def clearScreen():
    for i in range(0, 80): #'clears' the screen
        print("\n")
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def addToGuessesList(letter):
    
    GUESSES_LIST.append(letter)
"""-----------------------------------------------------------------"""

"""-----------------------------------------------------------------"""
def checkLetter(letter):

    indices = [i for i, x in enumerate(DICT_WORD) if x == letter]
    
    if not indices:
        return False

    for index in indices:
        GUESSED_WORD[index] = letter

    return True
"""-----------------------------------------------------------------"""

if __name__ == '__main__': 
    main()