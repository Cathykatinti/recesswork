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
#give a