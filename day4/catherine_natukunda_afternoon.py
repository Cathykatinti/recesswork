#arguments and paraments
#arguments always specified after the function name
#parameters are the actual value
def Afternoon():
    print("attendance is alwys close to 100")

def names(first_name, last_name):
    print(f"Hi{first_name}{last_name}")
    print("those are my names")
#calling a function
Afternoon()
names("catherine", "natukunda")

def Holidays(Cocis,Cedat):
   print(f"no holidys for{Cocis}  and{Cedat}")
Holidays("Bsse students","Civil students")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emilly", "Toby", "Linus")
#arguments with key values
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#default parameters

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#return keyword
def my_function(x):
  return 5 * x

print(my_function(3))
#arbitary keyword ,receives your dictionary arguements,this is when you dont know how many ketwords to pass in your arguements
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#using PASS TO A FUCTION TO AVOID ERRORS IF NO PARAMETERS ARE PASSES IN IT
#def myfunction():
 # pass

 #Recursion example
def my_recursion(t):
  if(t>1):
    result= t+my_recursion(t-1)
    print(result)
  else:
    result=0
    return result
  print("\n\nRecursion Exam")
  my_recursion(6) 
