''' 
CIS 122 Fall 2020 Lab 7
Author: Isabella Cortez
Credit: Lab Class
Description: Counts how many words start with each letter
'''

def palindrome(word):
    '''
    Description: returns individual letter of each word
    Args:
        word (str) = the words in the text file
    Returns:
        the individual letter of each word
    '''
    return word == word[::-1]

#variables
fin = open("words_alpha.txt")
counter = 0
longest = ""
shortest = ("asfjeifjidskfjeifejejfeilsjfiaefidfsiljadfjifsdijf")

#letters
counter_a = 0
counter_b = 0
counter_c = 0
counter_d = 0
counter_e = 0
counter_f = 0
counter_g = 0
counter_h = 0
counter_i = 0
counter_j = 0
counter_k = 0
counter_l = 0
counter_m = 0
counter_n = 0
counter_o = 0
counter_p = 0
counter_q = 0
counter_r = 0
counter_s = 0
counter_t = 0
counter_u = 0
counter_v = 0
counter_w = 0
counter_x = 0
counter_y = 0
counter_z = 0
num_palin = 0
other = 0

for line in fin:
    line = line.strip()
    counter += 1 
    if len(line) > len(longest):
        longest = line
    if len(line) < len(shortest):
        shortest = line
    if palindrome(line):
        num_palin += 1
    first_letter = line[0].lower()
    if first_letter == "a":
        counter_a +=  1
    elif first_letter == "b":
        counter_b += 1
    elif first_letter == "c":
        counter_c += 1
    elif first_letter == "d":
        counter_d += 1
    elif first_letter == "e":
        counter_e += 1
    elif first_letter == "f":
        counter_f += 1
    elif first_letter == "g":
        counter_g += 1
    elif first_letter == "h":
        counter_h += 1
    elif first_letter == "i":
        counter_i += 1
    elif first_letter == "j":
        counter_j += 1
    elif first_letter == "k":
        counter_k += 1
    elif first_letter == "l":
        counter_l += 1
    elif first_letter == "m":
        counter_m += 1
    elif first_letter == "n":
        counter_n += 1
    elif first_letter == "o":
        counter_o += 1
    elif first_letter == "p":
        counter_p += 1
    elif first_letter == "q":
        counter_q += 1
    elif first_letter == "r":
        counter_r += 1
    elif first_letter == "s":
        counter_s += 1
    elif first_letter == "t":
        counter_t += 1
    elif first_letter == "u":
        counter_u += 1
    elif first_letter == "v":
        counter_v += 1
    elif first_letter == "w":
        counter_w += 1
    elif first_letter == "x":
        counter_x += 1
    elif first_letter == "y":
        counter_y += 1
    elif first_letter == "z":
        counter_z += 1
    else:
        other += 1

# Results section
print("Count: " , counter)
print("Longest word is", longest + " ("+str(len(longest))+")")
print("Shortest word is", shortest + " ("+str(len(shortest))+")")
print("Palindromes:" , num_palin , "("+str(round(100*num_palin/counter, 2))+"%)")
print("A:",counter_a,"("+str(round(100*counter_a/counter,2))+"%)")
print("B:",counter_b,"("+str(round(100*counter_b/counter,2))+"%)")
print("C:",counter_d,"("+str(round(100*counter_c/counter,2))+"%)")
print("D:",counter_d,"("+str(round(100*counter_d/counter,2))+"%)")
print("E:",counter_e,"("+str(round(100*counter_e/counter,2))+"%)")
print("F:",counter_f,"("+str(round(100*counter_f/counter,2))+"%)")
print("G:",counter_g,"("+str(round(100*counter_g/counter,2))+"%)")
print("H:",counter_h,"("+str(round(100*counter_h/counter,2))+"%)")
print("I:",counter_i,"("+str(round(100*counter_i/counter,2))+"%)")
print("J:",counter_j,"("+str(round(100*counter_j/counter,2))+"%)")
print("K:",counter_k,"("+str(round(100*counter_k/counter,2))+"%)")
print("L:",counter_l,"("+str(round(100*counter_l/counter,2))+"%)")
print("M:",counter_m,"("+str(round(100*counter_m/counter,2))+"%)")
print("N:",counter_n,"("+str(round(100*counter_n/counter,2))+"%)")
print("O:",counter_o,"("+str(round(100*counter_o/counter,2))+"%)")
print("P:",counter_p,"("+str(round(100*counter_p/counter,2))+"%)")
print("Q:",counter_q,"("+str(round(100*counter_q/counter,2))+"%)")
print("R:",counter_r,"("+str(round(100*counter_r/counter,2))+"%)")
print("S:",counter_s,"("+str(round(100*counter_s/counter,2))+"%)")
print("T:",counter_t,"("+str(round(100*counter_t/counter,2))+"%)")
print("U:",counter_u,"("+str(round(100*counter_u/counter,2))+"%)")
print("V:",counter_v,"("+str(round(100*counter_v/counter,2))+"%)")
print("W:",counter_w,"("+str(round(100*counter_w/counter,2))+"%)")
print("X:",counter_x,"("+str(round(100*counter_x/counter,2))+"%)")
print("Y:",counter_y,"("+str(round(100*counter_y/counter,2))+"%)")
print("Z:",counter_z,"("+str(round(100*counter_z/counter,2))+"%)")
print("Other:",other,"("+str(round(100*other/counter,2))+"%)")

