from _functools import reduce
def update(n):
    return n+2
def is_even(n):
    return n%2==0
nums=[2,3,5,6,17,28,45,12,13]
evens=list(filter(lambda n:n%2==0,nums)) ## filter takes function,sequence
#evens=list(filter(is_even,nums))
print(evens)
# odds=list(filter(is_even,nums))
# print(odds)
## MAP--WHENEVER WE WANT TO CHANGE EVERY VALUE
doubles=list(map(update,evens))
print(doubles)
print(nums)
doubles=list(map(lambda x:x*2,nums))
print(doubles)
## REDUCE WE WILL GET ONLY ONE VALUE
def add_all(a,b):
    return a+b
sum=reduce(add_all,doubles)
print(sum)
sum=reduce(lambda x,y:x+y,doubles)
print(sum)