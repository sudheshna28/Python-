# name="sudheshna"
# age=23
# college="aditya"
# string="hi , %s!" %name
# print(string)

# var="eat"
# print("i like to %s chocolate ice creams" %var)
#
# string= "%s is %d year's old"%(name,age)
# print(string)
#
# x="dance"
# print("keerthi can %s and she can also %s" %(x,'sing'))
# print("the value off e is: %5.2f" %(246038.897928))


## format() method
# print("welcome to {} python tutorials".format("simplilearn"))
# s1="let 's {0} and {1} with simplilearn".format("learn","upskill")
# print(s1)
# print("{} called {} to inform that {} will be absent" .format("luke","daina","sudhi"))
# print("{1} called {2} to inform that {0} will be absent" .format("luke","daina","sudhi"))
# s2="{a},{b},{c} are very import to {d}.".format(a="machine learning",b="deep learning",c="neural networks",d="ai")
# print(s2)

## f-strings
# tutorial="python"
# place="simplilearn"
# subject="programming"
# print(f"let's learn {tutorial} {subject} from {place}")
# n1=60
# n2=12
# print(f" the product of {n1} and {n2} is {n1*n2}")
# num=50
# print(f" is number even? {True if num%2==0 else False}")

## Templace String
from string import Template
a1="python"
a2="simplilearn"
n=Template("hello welcome to $n1 programming by $n2")
print(n.substitute(n1=a1,n2=a2))

stu_name="sudheshna"
s=Template('hey $name! How are you?')
print(s.substitute(name=stu_name))







