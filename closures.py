def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner()  ## calling inner function
a=outer()
print(a)

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner  ## returns the reference of inner function to outer function
a=outer()
print(a())