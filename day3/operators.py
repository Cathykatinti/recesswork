"""
comparison operators
== equal to
!#add value:'+'
add and assign value: '+='
subtract and assign a value: '-='
multiply and assign value: '*='
divide and assign value '/='
modulus and assign value: '%='
exponentiate and assign value: '++='
Membership operators 
in :'in' operator checks 
identity operation: is :'is not' operator: checks 
if two values are the same or not
"""
#addition
"""x = 50+45
print(x)

#subtraction
y = 50-40
print(y)
#multipication
z = 50*40
print(z)
#Division
t = 50/2
print(t)
#Modulus
c = 10 % 3
print(c)
#Exponential
d = 2**4
print(d)
 #comparison operator
a= 15
b = 9
#greater than 
if a>b:
    print("true")
else:
    print("false")    
#less than
if a<b:
    print("true")
else:
        print("false")
#less than or equal to
if a<=b:
    print("true")
else:
    print("false")
#equal to
if a==b:
    print("true")
else:
    print("false")    
print(a<=b)  
y= 10
z= 35
if y != z:
    print("false")
else:
    print("true")  
#logical operator
a = True
b = False
#logical AND
if a and b:
    print("both are true")
else:    
    print("false")
#logical  OR
print(a or b)
#logical NOT
print(not a)
print(not b)
tea = True
cassava= False
print(not cassava)
#Assignment operator
#compound assignment
a=5
b = 10
z= 2
t = 10
e = 15
y = 4
#add and assign
a +=5
print(a)
a-=2
b -=1
z *=2
t /=2
e %= 2
y **=2
print(a)
print(b)
print(z)
print(t)
print(e)
print(y)
#membership assignment operator
cars =("Tx","Benz","toyota","Telsa","Jeep")
if "Benz"in cars:
    print("benz")
else:
    print("nont in")   
if "Bmw" in cars:
    print("it's there")
else:
    print("it's not there")      
#indentiy operators
x=10
y=10
print(x is y)
print(x is not y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
z =[1,2,3,4,5,6,7]
w =[1,2,3,4,5,6,7]
print(z is w)
print(z is not w)
#Bitwise operators
#used to perform operations on individual bits in binary
#Bitwise AND('&): Performs a bitwise AND operation betwee coresponding bits of two itegers
#Bitwise OR ('|'): performs
#Bitwise XOR('^'): performs a bitwise XOR operations
#bitwise NOT ('~')performs
#Bitwise left shift('<<') performes
#Bitwise right shift('>>')performs
#Bitwise operations
k= 10
j=20
result_and= k & j
print(result_and)
#exercise run for all
result_or = k|j
print(result_or)
result_xor = k ^j
result_not = k ~ j
result_left_shift = k<<j
"""
#example and assignments
#create a simple calculator function to calculate(and,subtract,multiply,divide)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main():
    a =int(input("enter the first number")) 
    b =int(input("enter the second number"))
    operator=input("enter the operator (+,-,*,/)")
if operator =='+':
    result = add(a,b)
elif operstor =='-':
    result = sub(a,b)

elif operstor =='*':
    result = multiply(a,b)
elif operstor =='/':
    result = divide(a,b)
else:
    print('invalid operator')

print("the result is ",result)
if_name == '_main_'
main()    
#tkinter learn
#assignment 1 a simple calculator program with a GUI inteface .make your title of the calculator 
#program with program window with your name eg cathy that performs add,sub,multiply and divide