## LAMBDA FUNCTIONS ARE THE ANONYMOUS  FUNCTIONS THAT ARE CREATED WITHOUT NAME  AND DEF KEYWORD
## CAN HAVE ANY NUMBER OF ARGUMENTS BUT CAN HAVE ONLY ONE EXPRESSION
# res=(lambda num,p : num**p)(3,2)
# print(res)
# res=(lambda num,den : num/den)(100,2)
# print(res)
# fun=lambda num,den : num/den
# res=fun(100,4)
# print(res)
# res1=fun(10,2)
# print(res1)

# add=lambda a,b:a+b
# res=add(3,4)
# print(res)

# add=lambda x:x+100
# x=int(input("enter a number:"))
# res1=add(x)
# print(f"Aftrer adding {x} with 100 the result is:{res1}")

# result=(lambda a,b :a*b)(3,4)
# print(result)
# product=lambda x,y,z:x*y*z
# print(product(z=5,y=6,x=10))  ## keyword arguments

# add=lambda x,y=10,z=4:x+y+z
# print(add(3))              ## default arguments

# addition=lambda *args:sum(args)
# print(addition(20,2,40,10))

# ## higher order function
# result= (lambda x,fun :x+fun(x))(20,lambda x:x*x)
# print(result)

# checker=(lambda x:('even' if x%2 ==0 else  'odd'))
# print(checker(15))

# sub_string=lambda string:string in "welcome to lambda functions"
# print(sub_string("lambda"))
list1=[10,28,37,48,59,65,74,20,23,12]
over_23=[]
greater_23=lambda x: x if x>23 else "not greater than 23"
for item in list1:
    over_23.append(greater_23(item))
print(over_23)

# numbers = [1, 2, 3, 4, 5]
#
# # Define a lambda function
# square = lambda x: x ** 2
#
# # Iterate through the list and apply the lambda function
# squared_numbers = []
# for number in numbers:
#     squared_numbers.append(square(number))
#
# print(squared_numbers)

list1=[10,28,37,48,59,65,74,20,23,12]
over_23=[]
for item in list1:
    if item>23:
        over_23.append(item)
    else:
        continue
print(over_23)
