"""
\w: matches any alphanumeric characters(a-z,A_Z,0-9 and underscore)
\s:matches any whitespace characters(space,tab,newline)
.:
\b:
\B:
[]:matches any character with in the brackect

"""
#example expressing regex|Match first word
import re
""""text = "hello,my name is cathy i am a programmer with no experience"
match = re.search(r"^\b\w+\b", text)
if match:
    print("Matches:",match.group())

matches = re.findall(r"\d+", text)
print("Matches:", matches.group())   

#ex2 validate email format or email address like cathynatukunda945@gmail.compile
def validate_email(email):
    pattern=r'^[\w\.]+@[\w\.]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
#ex of email
email = "cathynatukunda945@gmail.com"
email2 = "cathynatukcom"
print(validate_email(email,))
print(validate_email(email2))
    
#generators and iterators
# 'yield' generator
# iterator'__iter__''__next__'iterator
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    for i in range(1,10):
        print(factorial(i))        
def even_numbers_generator(n):
    for i in range(2, n+1, 2):
        yield i

# Example usage
generator = even_numbers_generator(10)

for num in generator:
    print(num)
#ex3
#generate function that yields the square of numbers from 1 to 10
for i in range(1,10):
 yield i**2
 #create an iterator object tht yields the square of num from 1-10
square_iterator = squares()
p#print the first five squares
for i in range(5):
    print(next(square_iterator))

#Decorator any decorator
#allows you modify a function behaviour or classes without directly changing their source code
def my_decorator(func):
    def inner():
        print("we deco")
        func()
        return inner
        @my_decorator
        def outer_decorator():
            print("we outer")

            outer_decorator()    
#decorators
#'@dcorator_name' is the name of the decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        #code to be executed before the original function
        print('this is my decorator before function execution')
        result = func(*args, **kwargs)
        print('after function result execution')
        #code to execute after the original func
        return result
    return wrapper    
@my_decorator
def my_function():
    print('inside the function')

my_function()    """

#example decorating classdef
def my_decorator(cls):
    class ModifiedClass:
        def __init__(self,*args,**kwargs):
            self.instances = cls(*args,**kwargs)

        def my_method(self):
            print("Modified class") 

    return ModifiedClass

@my_decorator 
class MyClass:
    def my_method(self):
     print("my original method")

my_instance = MyClass()
my_instance.my_method()

# 

