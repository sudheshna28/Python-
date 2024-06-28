import random
print("WELCOME TO ROCK PAPER SCISSORS GAME")
your_choice=int(input("Rock or Paper or Scissors:"))
print("your choice:",your_choice)
if(your_choice<0 or your_choice>2):
    print("You entered a wrong number,You Lose")
else:
    comps_choice=random.randint(0,2)
    print("computer choice:",comps_choice)
    if(comps_choice==your_choice):
        print("Match Draw")
    elif(comps_choice==0 and your_choice==2):
        print("You Win")
    elif(comps_choice==2 and your_choice==0):
        print("You Win")
    elif(comps_choice>your_choice):
        print("You Lose")
    else:
        print("You Win")




    

