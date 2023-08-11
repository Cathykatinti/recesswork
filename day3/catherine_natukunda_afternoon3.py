#exercise1
#1
names =["cathy","jemily","simon","cy","martin"]
print(names[1])
print(names[-4])
#2
new_name = "Katinti"
names[0]= new_name
print(names)
#4
names.insert(2,"Bathel")
print(names)
#3
names.append("jelly")
print(names)
#3
#qn5
names =["cathy","jemily","simon","cy","martin"]
names.remove("simon")
print(names)
#qn6
countries = ["Uganda","Nigeria","Kenya"]
print(countries[-1])
#qn7
new_list =["apple","pineapple","orange","Mango","Jackfruit","Guava","Passion"]
ran = new_list[3:6]
print(ran)
#qn8
countries = ["Uganda","Nigeria","Kenya"]
print(countries)
Africa = countries.copy()
print(Africa)
#qn9
for c in countries:
    print(c)
#10
Animals =["Cows","Goat","Elephant","Sheep"]
#ascending
Animals.sort() 
print(Animals)
Animals.sort(reverse=True)
print(Animals)  
#11
selected_items = list(filter(lambda item: 'a' in item, Animals))
print(selected_items) 
#qn 12
animals = ["cow","goat","pig"]
print(names + animals)
"""
#exercise 2
x = ("sumsung","iphone","tecno","redmi")
#1
print(x[3])
#2
print(x[-2])
x=  ("Techno","Iphone","Samsung")
#3
z = list(x)
z[1] ="itel"
x = tuple(z)
print(x)
#qn4
x = ("sumsung","iphone","tecno","redmi")
z = list(x)
z.append("Huawei")
x= tuple(z)
print(x)
#5
for phones in x:
    print(phones)
#6
del_list = list(x)
del_list.pop(0)
x=tuple(del_list)
print(x)
#7
tuple1 = (("Kampala","Mbarara","Gulu","Fortportal",'Hoima'))
#8
a,b,c,d,e = tuple1
print(a)
print(b)
print(c)
print(d)
print(e)
#9 2nd,3rd,4th
range1 =tuple1[2:4]
print(range1)
#10
name = ("catherine")
name1 = ("Natukunda")
names = name+name1
print(names)
#11
colors = ("red","blue","green")
mult_color = colors*3
print(mult_color)
#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
counting = thistuple.count(8)
print(counting)

#exercise 3
#1
beverages = set(("guiness","milkshake","cousins"))
print(beverages)
#2
beverages.update(("smirnoff","water"))
print(beverages)
#3
myset = {"oven","kettle","microwave","refrigerator"}
if ("microwave")in myset:
    print("it exists")
else:
    print("it's not there")    
#4 
myset.remove("kettle")
print(myset)
#5loop
for item in myset:
    print(item)
#6    
set1 = {"Bsse","Csc","Bist","Bram"}
list1=["computer","cocis"]
set1.update(list1)
print(set1)
set1.union(list1)
#7
set2 = {22,23}
set3 = {"cathy","natukunda"}
set4=set3.union(set2)
print(set4)
#exercise4
t = 20
z=  "name{}"
print(z.format(t))
#2
txt = " Hello, Uganda! "
print(txt.strip())
#3
print(txt.upper())
#4
new_txt = txt.replace('U', 'V')
print(new_txt)
#5
y= "I am proudly Ugandan"
range1 =y[1:4]
print(range1)
#
x = "All “Data Scientists” are cool!"
x = 'All "Data Scientists" are cool'
print(x)
#exercise 5
Shoes = {
"brand" : "Nick",
"color" : "black",
"size": 40
}
print(Shoes["size"])
Shoes["brand"]="Adidas"
print(Shoes)
#3
Shoes["type"]= "Sneakers"
print(Shoes)
#4
print(Shoes.keys())
#5
print(Shoes.values())
#6
if ("size") in Shoes:
    print("yes it exists")
#7loop
for x in Shoes:
    print(x)
#8
Shoes.pop("color")    
print(Shoes)
#9
Shoes.clear()
print(Shoes)
#10
League ={
    "premier":"Chelsea",
    "Africa":"Uganda_cranes",
    "School":"SLOSA"
}
League.copy()
print(League)
#11
myfamily = {
  "child1" : {
    "name" : "cathy",
    "year" : 2004
  },
  "child2" : {
    "name" : "Alban",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child1"]["year"])
"""