import random as rd

from hangman_words import wordlist
from hangman_pics import HANGMANPICS


#Choose a word randomly 
random_index = rd.randint(0, len(wordlist)-1)
word_random = wordlist[random_index]
word_length =  len(word_random)
#Test code 
print(f'Solution is {word_random}')
#display the  _ corresponding
string = len(word_random)*"_ "
list = string.split(" ")


end_game = False

# set lives to 6
lives = 6
pic_index = 0


#while loop
while not end_game : 
    #Ask the user to guess a letter
    guess = input("Guess the letter: ").lower()
    #replace the "_" by the matching letter in the word 
    for position in range(word_length):
        find = False
        if guess == word_random[position] :
            find = True
            list[position] = guess 



    if guess not in word_random:
        lives -= 1 
        pic_index +=1
        if lives == 0:
            end_game = True
            print("---------------------\nYOU LOOSE\n--------------------")


    #Display the list 
    print(' '.join(list))
    print(" ")
    print(f'lives remaining {lives}')
    print(HANGMANPICS[pic_index])


    if '_' not in list :
        end_game = True
        print("Gongratulations YOU WIN !!!!!!!!")


