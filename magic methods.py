list1=[1,2,4]
print(len(list1))
print(type(list1))
class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __len__(self):
        return self.pages
    def __str__(self):  ## return the string version of any object
        return f"{self.book_name} by {self.name}"
    def __call__(self,*args,**kwargs):
        print("hiii")
    def __del__(self):
        print("Author's object has been deleted")
d=Author("sudheshna","python basic to advance", 500)
print(len(d))
print(d)
d()
del d
print(d)
# print(str(d))
 ## prints the dunder methods of int class
methods=dir(int)
print(methods)
print(len(methods))
