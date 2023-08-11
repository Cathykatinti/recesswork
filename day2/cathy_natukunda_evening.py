#dictionary is a collection unordered,changeable and indexed
#has keys and values
University= {
    "Makerere":"software_engineering",
    "Ndejje":"Civil Engineering",
    "Mbarara":"Medicine",
    "Gulu":"Clinical",
    "Busitema":"Biomedical"
}
print(University)
#accesing items in a dictionary
y = University["Ndejje"]
print(y)
#accessing items using the get()methods
x = University.get("Mbarara")
print(x)
#changing value of a specific item using its key
University["Gulu"]="surgery"
print(University)
#updating (adding a value)a dictionary you use a new key and assign a value to it
University["Nkumba"] = "Architecture"
print(University)
#updating the dictionary using the update function
new_dict ={
    "Kabale": "Education",
    "Nkozi":"Building"
}
Institutes ={
    "Ymca":"Design",
    "Nakawa":"IT",
    "Buganda":"Baking"
}
University.update(new_dict)
print(University)
#accessing keys looping throu them
for x in University:
 print(x)
 #accesing values-looping through
 for x in University:
    print(University[x])
#use the values() method to return a list of all values
for x in University.values():
    print(x)
#looping through keys and values at the same time using the items()
for x, y in University.items():
  print(x, y)
#removing
#1 pop removes the item with a specific key name
"""University.pop("Nkozi")
 print(University)

#2 popitem removes the last inserted item though initially it would remove any random item
Institutes.popitem()
print(Institutes )
"""
#3 del removes item with a specified key and can delete the dictionary completely
del Institutes["Buganda"]
print(Institutes)
#4 clear empties the dictionary
Institutes.clear()
print(Institutes)
#check if a key does exit in your dictionary
if "Makerere" in University:
    print("yes")
else:
    print("no")   
#checking the length of a dictionary
print(len(University)) 
#numbers
#there are three main types of numbers i.e int,Float,Complex
w = 10 #int
r = 3.9 #float
s = 2j #complex
print(type(w))
print(type(r))
print(type(s))
#integers
a = 2
b = 5678901233
c = -56433
print(type(a))
print(type(b))
print(type(c))
#complex
w = 6+10j
t = 4j
h = -2j

print(type(w))
print(type(t))
print(type(h))
#type conversion
y = 10#int
r = 3.9#float
s = 2j#complex
#convert from int to complex
z = complex(y)
print(z)
print(type(y))
#casting
#works mostly when you want to specify a variable type
h = int(10)
y = int(30000000)
a = int("8")
print(h)
print(y)
print(a)
#String
print("Afternoon")
print('Afternoon')
w = "Names"
print(w)
#multiline strings
q = """I am offering BSSE year three 
currently doing recess in python,
Data Science,Django"""
print(q)
#strings as array
a = "Afternoon"
print(a[0])
print(a[4])
print(a[-1])
#exercise 1 using the len function to determine the length of the string
print(len(q))
print(len(w))
#exercise2 using for loopin string - its to iterate through
for y in a:
    print(y)
#exercise3 of slicing strings
# used to return a range of characters by using the slicing syntax,u specify the beginning and end index
b = "We try again tommorrow"
print(b[1:5]) 
print(b[6:12])
print(b[2:])
print(b[5:])
#modifying strings
q = "Names"
print(q.lower())
print(q.upper())
#remove white space at the end and beginning
b =" status "
print(b.strip())
text = "Hello bsse"
new_text = text.replace("bsse","Cathy")
print(new_text)
#string concatenation
w = q+b#w = q +""+ b
print(w)
#format
#works when you want to combine a string to a number
age = 20
txt = "My name is John, I am {}"
print(txt.format(age))
#bolean
#these evaluate to true or false
print(20<10)
print(30==40)
print(30>10)
print(bool(15))
r = "cathy"
z= 30
print(bool(r))
print(bool(z))
#exercise use a condition to show how to use boleans
is_raining = True
is_sunny = False
if is_raining:
    print("remember to take an umbrella")
if is_sunny:
    print("Dont forget your sun glasses")
if not is_raining and not is_sunny:
    print("it seems to cloudy")   
temp = 25
is_hot= temp>30
is_cold = temp<15
if is_hot:
    print("it's a hot day!")
elif is_cold:
        print("it's a cold day!")
else:
            print("its a moderate day")
