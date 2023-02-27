''' 
CIS 122 Fall 2020 Assignment 5
Author: Isabella Cortez
Credit: Tori Walters, Jasmine Wallin, Lauren Mathews
Description: Create a guessing game that allows an user to input a letter in order to guess a word (kind of like online hangman)
'''

word = input
guess = input

def game(word, guess, case_sensitive = False):
    '''
    This function takes in a word and letter and makes sure they are not case sensitive, in order for the user to guess a word
    Args:
        word = the word the user inputs
        guess = the guessing letter the user inputs to find the word
    Returns:
        None
    '''
    
    # defined variables
    allGuesses = 0
    matched = ''
    unmatched = ''

    quit = False

    while True:
        # allows the user to input a word
        word = input("Enter a guess word (Press enter to quit): ")


        if len(word) > 0:
            break
        else:
            quit = True
            break
        
    if not quit:
        targetString = ''
        for character in word:
            if character not in targetString:
                targetString += character

    while True:
        # allows the user to input a letter
        guess = input("Enter a guess letter (Press enter to quit): ")

        # makes sure the input is not case sensitive
        if not case_sensitive:
            word = word.lower()
            guess = guess.lower()

            # enter to quit (guess/letter)
            if guess == '':
                break
            elif len(guess) > 1:
                print('\t>only a single letter can be used')

            else:
                # checks to see if it is in the letter bank and adds to the guesses
                if guess in unmatched:
                    allGuesses += 1
                    print('\t>Guessed letter: ' + guess + ' not found')
                    print('\t>Guesses so far ' , matched + unmatched)
                    
                elif guess in matched:
                    allGuesses += 1
                    print('\t>Guessed letter: ' + guess + ' already found')
                    print('\t>Guesses so far ' , matched + unmatched)
                    
                elif guess not in word:
                    unmatched += guess
                    allGuesses += 1
                    print('\t>Guessed letter: ' + guess + ' not found')
                    print('\t>Guesses so far: ' , matched + unmatched)
                    
                else:
                    matched += guess
                    allGuesses += 1
                    print('\t>Guessed letter: ' + guess + ' found')
                    print('\t>Guesses so far: ' , matched + unmatched)


                # if the word matches the guesses 
                if len(matched) == len(targetString):
                    break
                

    
print(' ')
print('*** Results ***')
print('Word: \t' , word)
print('Matched: \t' , matched)
print('Unmatched: \t' , unmatched)
print('Guesses: \t' , allGuesses)

game(word, guess)
