# def str_upper(func):
#     def inner():
#         str_1=func()
#         return str_1.upper()
#     return inner
# @str_upper
# def print_str():
#     return "good morning"
# # res_1=str_upper(print_str)
# print(print_str())


def decorator_fun(f):
    def wrapper(x,y):
        if(x%2==0 and y%2==0):
            f(x,y)
        else:
            print("Enter Only Even Numbers")
    return wrapper



# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
@decorator_fun
def sum(a,b):
    print(a+b)
sum(2,8)