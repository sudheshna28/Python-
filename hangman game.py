print("welcome To Hangman Game")
print("Guess The Letter")
print("You Have Only 6 Lives If You Lose Your Lives Will Be Decreased")
import random
words_list=["scary","cheerfull","amazon","modest","mirchi","apple","banana","carrot","donkey","elephant","fish","sun","hen","igloo","jar","car","kite","lemon","mount","naughty","xerox","zebra","tree","ribbon","ostrich","parrot","penguin","qatar","Ahmedabad","shiridi","jungle","tirupati","varanasi","india","nepal","america","swiss","fuzi","forest","terrible","upon","humble","uncle"]
lives=6
#print(len(words_list))
random_word=random.choice(words_list)  ##swiss
##print(random_word)
len_word=len(random_word)  ##5
blank_word=len_word*["_"] 
print(blank_word)   
game_over=False
while not game_over:
    guess_letter=input("Guess A Letter:")  ##s
    for position in range(len(random_word)):  ##(0,4),0
        letter=random_word[position]  
        if letter==guess_letter:
            blank_word[position]=guess_letter
            print(blank_word)
    if guess_letter not in random_word:
        lives-=1
        print("You have only ",lives,"lives")
        if lives ==0:
            game_over=True
            print("Out Of Lives")
            print("You Lost")
            ##print("Soryy The Word Is",random_word)
    if "_" not in blank_word:
        game_over=True
        print("Congratulations,You Guessed The Word Correctly")
        print("You Won")
       ## print("Soryy The Word Is",random_word)
