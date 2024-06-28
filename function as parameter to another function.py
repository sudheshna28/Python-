def function1():
    print("hi i am function1")
def function2(func):
    print("hi i am function 2 now i call function1")
    func()
    ##func and function1 have same id
    # print(id(function1))
    # print(id(func))
function2(function1)
