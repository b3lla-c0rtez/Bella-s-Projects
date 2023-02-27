''' 
CIS 122 Fall 2020 Lab 7
Author: Isabella Cortez
Credit: Lab Class
Description: Checks to see if a certain word is in the text file
'''

fin = open("words_alpha.txt")

while True:
    word = input("Enter search word (blank to quit): ")
    found = False

    if len(word) == 0:
        break

    for line in fin:
        if word == line.strip():
            found = True
            break
    fin.close()

    if found:
        print(word + " found")
    else:
        print(word + " not found")
