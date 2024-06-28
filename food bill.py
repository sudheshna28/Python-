import random
names=input("Enter Everybody name's:")
splitted_list=names.split(",")
bill=random.randint(0,6)
print(bill)
print(splitted_list)
if(bill==0):
    print(f"{splitted_list[0]} will pay the bill")
elif(bill==1):
    print(f"{splitted_list[1]} will pay the bill")
elif(bill==2):
    print(f"{splitted_list[2]} will pay the bill")
elif(bill==3):
    print(f"{splitted_list[3]} will pay the bill")
elif(bill==4):
    print(f"{splitted_list[4]} will pay the bill")
elif(bill==5):
    print(f"{splitted_list[5]} will pay the bill")
elif(bill==6):
    print(f"{splitted_list[6]} will pay the bill")
else:
    print("WAITER HAS TO PAY THE BILL")
    
                            ##JENNYS CODE
length=len(splitted_list)
random_choice=random.randint(0,length-1)
print(f"{splitted_list[random_choice]} will pay the bill")
