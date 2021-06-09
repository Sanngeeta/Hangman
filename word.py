import string 
import random


def load_words():


    WORDLIST_FILENAME = "words.txt"
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    word_list = line.split()

    return word_list 
    
load_words()

def choose_word():

    word_list=load_words()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()

    return secret_word

choose_word()
    
