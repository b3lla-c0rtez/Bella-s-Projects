''' 
CIS 122 Fall 2020 Assignment 3 Question 1
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews, Jasmine Wallin, Estella Pryor
Description: Create a function with one for loop that reverses a sentence
'''

def reverse(original_sentence):
    
    """
    we are making a sentence reverse/making a sentence print backwards

    the for loop takes the original sentence and does i + reverse_sentence in order to reverse the sentence. it then reverses the sentence. the output shows the first sentence and the second print statement calls the reverse function which flips the first sentence around/or makes it go backward/reverses it

Args:
   original_sentence(string): that is the first sentence/the sentence that is not reversed

Returns:
   reversed_sentence
    """
    
    reversed_sentence = ""
    for i in original_sentence:
        reversed_sentence = i + reversed_sentence # reverses it
    return reversed_sentence
original_sentence = "When in the Course of human events" # the sentence

print("Original: " , original_sentence)
# prints the sentence
print("Reversed: " , reverse(original_sentence))
# prints the sentence but it is backwards
