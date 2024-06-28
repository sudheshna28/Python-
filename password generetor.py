import random
print("Welcome To Passoword Generator")
letters=['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' ,'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'x' , 'y' ,  'z',
            'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U',
            'V' , 'X' , 'Y' ,  'Z']
numbers=['0' , '1', '2', '3', '4', '5', '6', '7','8', '9']
symbols=["!","@","#","$","%","&","(",")","_"]
n_letters=int(input("enter the no of letters you want:"))
n_numbers=int(input("enter the no of numbers you want:"))
n_symbols=int(input("enter the no of symbols you want:"))
password=[]
for i in range(1,n_letters+1):
    character=random.choice(letters)
    password+=character
##    print(character)
##    print(type(character))
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    password+=num
for i in range(1,n_symbols+1):
    spl=random.choice(symbols)
    password+=spl
##print(password)
random.shuffle(password)
##print(password)
pass_word=""
for item in password:
    pass_word+=item
print(pass_word)
