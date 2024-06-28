# ## zip() takes a number of iterables and then creates a tuple from each element of the itrables,like map() in python3 it returns generator object and than can be easily converted into list
# a=[1,2,3,4,5]
# b=['s','p','q','d',"a"]
# result=list(zip(a,b))
# print(result)

a=[1,2,3,4,5]
b=['s','p','q','d']
result=list(zip(a,b))
print(result)
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1, 2, 3, 4, 5]
# res=lambda my_strings,my_numbers:(my_strings,my_numbers)
# print(list(res))
# # results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
# # print(results)