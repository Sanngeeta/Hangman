import string
from word import choose_word
from images import IMAGES


def ifValid(user_input):
    if len(user_input) != 1:
        return False
    # if not user_input.isalpha():
    #     return False
    # return True 

def is_word_guessed(secret_word,letters_guessed):
    if secret_word==get_guessed_word(secret_word, letters_guessed):
        return True
    return False


def get_guessed_word(secret_word,letters_guessed):
# ye while hamare sciret word ki lenth batata hai
    i=0
    guessed_word=""
    while i<len(secret_word):
        if secret_word[i] in letters_guessed:
            guessed_word+=secret_word[i]
        else:
            guessed_word+="_"
        i=i+1
    return guessed_word

# ye hamare pass avileble letter kitane hai wo batayga
def get_available_letters(letters_guessed):
    import string
    letters_left=string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,"")
    return letters_left


def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)
    return random.choice(letters_not_guessed)


def hangman(secret_word):
    
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("") 

    letters_guessed = []
    remaining_lives=8
    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]
    level=input("enter the level in which you want to pay:""\n""(a) for esay""\n""(b) for medium""\n""(c) for hard level :-")
    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[1,2,3,4,5,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        image_selection=[1,3,5,7]
    else:
        if level!="a":
            print("your choice is in vaild"" \n ""game is starying in easy level")


    while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)

        guess = input("Please guess a letter: ")
        letter = guess.lower()
         
        if (not ifValid(letter)):
            pass
            # print("Invalid input")
            
        

        if guess=="hint":
            print("your hint for secret word is :-"+get_hint(secret_word, letters_guessed))
        else:
                
            # if (not ifValid(letter)) and letter!="hint":
            #     print("Invalid input")
            #     continue   

            if letter in secret_word:
                letters_guessed.append(letter)
                print ("Good guess: " + get_guessed_word (secret_word , letters_guessed ))
                print ("")
                    

                if is_word_guessed(secret_word, letters_guessed) == True:
                    print (" * * Congratulations, you won! * * ")
                    print ("")
                    break

                    

            else:                                                                                              
                print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                letters_guessed.append(letter)
                print(IMAGES[8- remaining_lives])
                # print(IMAGES[image_selection[total_lives-remaining_lives]])
                remaining_lives-=1
                print("remaining_lives: "+str(remaining_lives))
                print( ""  )

    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")


secret_word=choose_word()
hangman(secret_word)