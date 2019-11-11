# Problem Set 2, hangman.py
# Name: David Smith
# Collaborators: None
# Time spent: I'd rather not say...

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import msvcrt as m

# fix top_score
# fix hint (*) function

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return_string = ''
    for i in secret_word:
        if i in letters_guessed:
            return_string += i
        else:
            return_string += ' _ '
    return return_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return_string = ''
    available_letters = string.ascii_lowercase
    for i in available_letters:
        if i in letters_guessed:
            continue
        return_string += i
    return return_string


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (
                my_word[i] != other_word[i] \
                or my_word.count(my_word[i]) != other_word.count(my_word[i]) \
            ):
                return False
        return True
            

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    words_list = open(WORDLIST_FILENAME, 'r').readline().split()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
    print(possible_matches)
      
        
    
def game_over():
    divider = '\n=============================================================\n'
    print(divider)
    print('Bad luck! You ran out of lives.')
    print('.·´¯`(>▂<)´¯`·.')
    print('The secret word was ' + secret_word + '.')
    print('Game over.')
    print(divider)
    

def play_game():
    warnings = 3
    lives = 6
    divider = '\n=============================================================\n'
    print('The secret word contains ' + str(len(secret_word)) + ' letters.')
    print(divider)
    print('You have 6 lives.')
    print('Available letters: ' + get_available_letters([]))
    print(divider)
    user_input = input('Guess a letter. ')
    guess = user_input.lower()
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while lives > 0:
        if (guess.isalpha() == False and lives == 1) or (guess in letters_guessed and lives == 1):
            return game_over()
            break
        if (guess.isalpha() == False and warnings == 1) or (guess in letters_guessed and warnings == 1):
            lives -= 1
            print(divider)
            print('No warnings left. Lose a life.')
            print(divider)
            user_input = input('Guess a letter. ')
            guess = user_input.lower()
        elif guess.isalpha() == False and warnings > 1:
            warnings -= 1
            if warnings == 1:
                print(divider)
                print('That is not a valid letter. ' + str(warnings) + ' warning left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print(divider)
                print('That is not a valid letter. ' + str(warnings) + ' warnings left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in letters_guessed and warnings > 1:
            warnings -= 1
            if warnings == 1:
                print(divider)
                print('You\'ve already guessed that letter. ' + str(warnings) + ' warning left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print(divider)
                print('You\'ve already guessed that letter. ' + str(warnings) + ' warnings left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in secret_word:
            letters_guessed += guess
            if is_word_guessed(secret_word, letters_guessed):
                print(divider)
                print('Well done! You guessed the secret word!')
                print('＼(＾O＾)／')
                print('The secret word was ' + secret_word + '.')
                score = lives*len(secret_word)
                print('Score: ' + str(score))
                if score > top_score:
                    top_score = score
                    print('***New top score!***')
                    print(divider)
                break
            else:
                print(divider)
                print('Nice!\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in vowels:
            print(divider)
            print('Nup, not in there. That was a vowel so you lose 2 lives!' + '\n')
            letters_guessed += guess
            lives -= 2
            if lives <= 0:
                return game_over()
                break
            elif lives == 1:
                print('You have ' + str(lives) + ' life left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print('You have ' + str(lives) + ' lives left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        else:
            print(divider)
            print('Nup, not in there. That was a consonant so you lose 1 life.')
            letters_guessed += guess
            lives -= 1
            if lives <= 0:
                return game_over()
                break
            elif lives == 1:
                print('You have ' + str(lives) + ' life left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print('You have ' + str(lives) + ' lives left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()


def play_game_hints_active():
    top_score = 0
    warnings = 3
    lives = 6
    divider = '\n=============================================================\n'
    print('The secret word contains ' + str(len(secret_word)) + ' letters.')
    print(divider)
    print('You have 6 lives.')
    print('Available letters: ' + get_available_letters([]))
    print(divider)
    
    user_input = input('Guess a letter. ')
    guess = user_input.lower()
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while lives > 0:
        if guess == '*':
            print('Possible matches: \n')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print(divider)
            user_input = input('Guess a letter. ')
            guess = user_input.lower()
        elif (guess.isalpha() == False and lives == 1) or (guess in letters_guessed and lives == 1):
            return game_over()
            break
        elif (guess.isalpha() == False and warnings == 1) or (guess in letters_guessed and warnings == 1):
            lives -= 1
            print(divider)
            print('No warnings left. Lose a life.')
            print(divider)
            user_input = input('Guess a letter. ')
            guess = user_input.lower()
        elif guess.isalpha() == False and warnings > 1:
            warnings -= 1
            if warnings == 1:
                print(divider)
                print('That is not a valid letter. ' + str(warnings) + ' warning left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print(divider)
                print('That is not a valid letter. ' + str(warnings) + ' warnings left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in letters_guessed and warnings > 1:
            warnings -= 1
            if warnings == 1:
                print(divider)
                print('You\'ve already guessed that letter. ' + str(warnings) + ' warning left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print(divider)
                print('You\'ve already guessed that letter. ' + str(warnings) + ' warnings left.')
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in secret_word:
            letters_guessed += guess
            if is_word_guessed(secret_word, letters_guessed):
                print(divider)
                print('Well done! You guessed the secret word!')
                print('＼(＾O＾)／')
                print('The secret word was ' + secret_word + '.')
                score = lives*len(secret_word)
                print('Score: ' + str(score))
                if score > top_score:
                    top_score = score
                    print('***New top score!***')
                    print(divider)
                break
            else:
                print(divider)
                print('Nice!\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        elif guess in vowels:
            print(divider)
            print('Nup, not in there. That was a vowel so you lose 2 lives!')
            letters_guessed += guess
            lives -= 2
            if lives <= 0:
                return game_over()
                break
            elif lives == 1:
                print('You have ' + str(lives) + ' life left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print('You have ' + str(lives) + ' lives left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
        else:
            print(divider)
            print('Nup, not in there. That was a consonant so you lose 1 life.')
            letters_guessed += guess
            lives -= 1
            if lives <= 0:
                return game_over()
                break
            elif lives == 1:
                print('You have ' + str(lives) + ' life left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
            else:
                print('You have ' + str(lives) + ' lives left.\n')
                print(get_guessed_word(secret_word, letters_guessed) + '\n')
                print('Available letters: ' + get_available_letters(letters_guessed))
                print(divider)
                user_input = input('Guess a letter. ')
                guess = user_input.lower()
    

def wait():
    m.getch()
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    rules = '''
    * In this version of Hangman
    you start with 6 lives and 3 warnings.
    * If you input anything besides an alphabet character you lose a warning.
    * If you lose all your warnings you lose a life.
    * If you guess an incorrect consonant you lose a life.
    * If you guess an incorrect vowel you lose two lives.
    * If you lose all your lives you lose the game.
    * See https://en.wikipedia.org/wiki/Hangman_(game)
    for more information about the game.
    '''
    warnings = 3
    lives = 6
    print('Welcome to the game Hangman!')
    rules_q = input('Would you like to know the rules? Type y or n followed by enter. ')
    rules_lower = rules_q.lower()
    while True:
        if rules_lower == 'n':
            hints_q = input('Would you like to activate hints? Type y or n followed by enter. ')
            hints_lower = hints_q.lower()
            if hints_lower == 'y':
                return play_game_hints_active()
            elif hints_lower == 'n':
                return play_game()
            else:
                print('That is not a valid choice. Please choose again. \n')
                hints_q = input('Would you like to activate hints? Type y or n followed by enter. ')
        elif rules_lower == 'y':
            print(rules)
            proceed = input('Press enter to continue. ')
            return wait()
        else:
            print('That is not a valid choice. Please choose again. \n')
            rules_q = input('Would you like to know the rules? Type y or n followed by enter. ')
            rules_lower = rules_q.lower()
    
    
            
if __name__ == "__main__":

    #edited so that hangman() offers choice of hints enabled or disabled
    #previously there was hangman() and hangman_with_hints()
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
