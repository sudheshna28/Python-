def outer():
    print("outer function execution")
    def inner():
        print("inner function execution")
    inner()
    print("outer function body")
outer()
# ## here in above example  inner() is local to outer() so we can not call inner() outside the outer() function

# def outer():
#     print("outer function execution")
#     def inner():
#         print("inner function execution")
#     print("outer function after inner functions")
#     return inner
# f1=outer()
# f1()
# f1()
# f1()