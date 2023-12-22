import sys
from sys import stdin
'''
iterate through all possible prefixes of input string
for every prefix, extract suffix
got help from Samuel Davis after my recursive function did not work
'''

def splitWordsIterative(w: str, dict):
    word_length = len(w)
    table = [[] for i in range(word_length+1)]
    table[0] = [[]]
    for i in range(word_length):
        for j in range(i+1):
            split_word = w[j:i+1]
            # stuff = w[i+1:]
            if split_word in dict:
                if table[j]:
                    for split in table[j]:
                        table[i+1].append(split+[split_word])
    if table[word_length]:
        return min(table[word_length], key=len)
    else:
        return None



'''
def splitWordsRecursive(w: str, dictCon):
    word_length = len(w)
    if word_length == 0:
        return True

    word_break = [False for i in range(word_length+1)]
    for i in range(1, word_length+1):
        if word_break[i] == False and w[0:i] in dictCon:
            word_break[i] = True

        if word_break[i] == True:
            if i == word_length:
                return True


            for j in range(i+1, word_length+1):
                if word_break[j] == False and w[i:j] in dictCon:
                    word_break[j] = True

                empty_list = []
                if word_break[j] == True and j == word_length:
                    empty_list.append([w[i:j]])
                    return empty_list
                    # return splitWords(w[i:j], dictCon)
    return None
'''

if __name__  == '__main__':
    linenum = int(sys.stdin.readline().strip())
    with open("diction10k.txt", "r") as file:
        words = set(file.read().split())
    for line in range(linenum):
        phrase = sys.stdin.readline().strip()
        seq = splitWordsIterative(phrase, words)
        if seq is None:
            print(f"Phrase {line+1}")
            print(phrase + '\n')
            print(f"Output {line+1}")
            print("NO, cannot split\n")
        else:
            print(f"Phrase {line+1}")
            print(phrase + '\n')
            print(f"Output {line+1}")
            print("YES, you can split")
            print(' '.join(seq) + '\n')
