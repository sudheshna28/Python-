##small pizza=100
##medium pizza=200
##large pizza=300
##pepporoni for small pizza=30
##pep ->medium or large  =50
##pep->extra cheese=20
print("Welcome to Python Pizza")
bill=0
pizza_size=input("enter the size of pizza you want:")
if(pizza_size=="small"):
    print("small pizza is 100 rupees")
    bill+=100
    pepporoni=input("want any pepporoni:")
    if(pepporoni=="y"):
        print("pepporoni costs 30 rupees extra")
        bill+=30
    else:
        bill=100
elif(pizza_size=="medium"):
    print("medium pizza is 200 rupees")
    bill+=200
    pepporoni=input("want any pepporoni:")
    if(pepporoni=="y"):
        print("pepporoni costs 50 rupees extra")
        bill+=50
    else:
        bill=200    
else:
    print("large pizza is 300 rupees")
    bill+=300
    pepporoni=input("want any pepporoni:")
    if(pepporoni=="y"):
        print("pepporoni costs 50 rupees extra")
        bill+=50
    else:
        bill=300
extra_cheese=input("want any extra cheese:")
if(extra_cheese=="y"):
    print("cheese costs 20 rupees extra")
    total_bill=bill+20
else:
    total_bill=bill
print(f"your total bill is:{total_bill}")
    








    
