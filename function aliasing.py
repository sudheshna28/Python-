def greet(name):
    print("hello!!",name)
wish=greet
print(id(wish))  ## both ids are same
print(id(greet))
wish("sudheshna")
del greet
greet("sudheshna")


