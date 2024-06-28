import random
##import logo
print("GUESS THE NUMBER")
##print(logo.logo)
print("Let Me Think Of  A Number Between 1 to 50.")
level=input("Choose level of difficulty..Type 'easy' or 'hard':")
random_number=random.randint(1,51)
if level=='easy':
    count=10
    for chance in range(0,11):
        guessed_number=int(input("Make  A Guess:"))
        if guessed_number<random_number:
            print("Your guess is too low")
            count=count-1
            print(f"you have only {count} chances to guess a number")
        elif guessed_number>random_number:
            print("Your guess is too high")
            count=count-1
            print(f"you have only {count} chances to guess a number")
        else:
            print("your guess is right... The answer is",guessed_number)
            break
    if count==0:
        print("You Loose the random number is",random_number)
elif level=='hard':
    count=5
    for chance in range(0,5): 
        guessed_number=int(input("Make A Guess:"))
        if guessed_number<random_number:
            print("Your guess is too low")
            count=count-1
            print(f"you have only {count} chances to guess a number")
        elif guessed_number>random_number:
            print("Your guess is too high")
            count=count-1
            print(f"you have only {count} chances to guess a number")
        else:
            print("your guess is right... The answer is",guessed_number)
            print("You Won")
            break
    if count==0:
        print("You Lost random number is", random_number)
        
