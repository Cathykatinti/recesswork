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

