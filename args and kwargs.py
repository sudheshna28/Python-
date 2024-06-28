##def add(*numbers):#3
##    c=0
##    ##print(name)
##    print(numbers)
##    for i in numbers: ##(0,2)
##        c=c+i ## c=0+1=1,c=1+2=3,3+9=12
##    print(c)
####add(1,2,3,5,9,"sudhi")##sudhii is taking in tuple numbers but not as another parameter
##add(1,23,67,32)
##add(1,2,9)

##def add(*numbers,name):#3
##    c=0
##    print(numbers)
##    print(name)
##    for i in range(0,len(numbers)): 
##        c=c+numbers[i]
##    print(c)
##add(1,2,3,5,9,name="sudhi")
##
##

##first pass positional and then arbitrary 
##def add(name,*numbers):#3
##    c=0
##    print(name)
##    for i in range(0,len(numbers)): ##(0,2)
##        c=c+numbers[i] ## c=0+1=1,c=1+2=3,3+9=12
##    print(c)
##add("sai",1,2,3,5,9)

def info_person(*args,**info):  ##passed as dictionary
    print("args",args)
    for key,value in info.items():
        print("dicts",key,value)
info_person(8,8,num=9,name="sudheshna",age=28,dept="cse")
##info_person(9,5,7,name="ram",dept="salesforce",salary=78000)

            
    
    


