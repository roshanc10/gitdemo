#fuction call

name="roshan"
def sayHello(name):
    print (" hello " + name)

sayHello(name)

#default fucntion call , in above if we use name in the function call it gets hello roshan called
def sayHello(name=" new customer"):
    print (" hello " + name)

sayHello()

#to access docstring in python functionname._doc_
def sayHello(name=" new customer"):
    "this is an example"
    print (" hello " + name)
print(sayHello.__doc__)

#sumfunction
def sumParameter(arg1,arg2):
    result=arg1+arg2
    return  result
summation=sumParameter(2,5)
print (summation)

#lambda
summ=lambda x,y:x+y
print(summ(5,6))