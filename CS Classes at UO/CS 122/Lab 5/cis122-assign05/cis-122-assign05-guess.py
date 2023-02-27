''' 
CIS 122 Fall 2020 Assignment 5
Author: Isabella Cortez
Credit: Tori Walters, Jasmine Wallin, Lauren Mathews
Description: Create a guessing game that allows an user to input a letter in order to guess a word (kind of like online hangman)
'''

#define variables 
guess = input
word = input

def game(word, guess, case_sensitive = False):
    '''
    This function takes in a word and letter and makes sure they are not case sensitive, in order for the user to guess a word
    Args:
        word = the word the user inputs
        guess = the guessing letter the user inputs to find the word
    Returns:
        None
    '''
   
    #define variables
    allGuesses =  0
    matched = ""
    unmatched = ""

    quit = False
    
    while True:
        word = input("Enter a guess word (blank to quit): ")

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

    #write statments for if code is blank or larger than one
    while True:
 
        guess = input("Enter a guess letter (blank to quit): ")
        
        if not case_sensitive:
            word = word.lower()
            guess = guess.lower()

        if guess == " ":
            break

        elif len(guess) > 1:
            print("Only single letters can be guessed.")

        elif word == " ":
            break

        #conditionals to find if letter is in word and is matched or not.
        else:

            if guess in unmatched:
                allGuesses += 1
                print("\t >Guessed letter " + guess + " found in word.")
                print("\t >Guesses so far: " , matched + unmatched)

            elif guess in matched:
                allGuesses += 1
                print("\t >Guessed letter " + guess + " already found in word.")
                print("\t >Guesses so far: " , matched + unmatched)

            elif guess not in word:
                unmatched += guess
                allGuesses += 1
                print("\t >" + guess + " not found.")
                print("\t >Guesses so far: " , matched + unmatched)

            else:
                allGuesses += 1
                matched += guess
                print("\t >Guessed letter " + guess + " found in word.")
                print("\t >Guesses so far: " , matched + unmatched)

            if len(matched) == len(targetString):
                break
    
    #print statements
    print(" ")
    print("*** Results ***")
    print("Word:     \t " , word)
    print("Matched:\t " , matched)
    print("Unmatched:\t " + unmatched)
    print("Guesses:\t ", allGuesses)
        
#Test function
game(word, guess)
