#for and while loop
"""
seq = ["pinapple","apple","Mango"]
for i in seq:
    print(seq)

#while loop
#while condition prints a condition aslong as a certain condition is true
#example
x = 0
while x <5:
    print(x)
    x+=1
# break and continue

for number in range(1,10):
    if number == 5:
        break
    print(number)   
for number in range(10,30):
    if number == 15:
        continue
    print(number) 
    try:
         x= 10/0
    except ZeroDivisionError:
        print('error:Division by zero')      
    finally:
        print('this is always executed')
        """
emotion = {
    'happy': " I am glad to hear you are happy",
    'sad':"why aren't you happ",
    'angry':"you will be fine",
    'fearful': "listen to music",
    'disqusted':" tha's bad"
}
    #prompt the user to enter their emotions
user_emotion = input("how are you feeling today?")
#convert the user input to lowercase
"""user_emotion = user_emotion.lower
if user_emotion in emotion:
    print(emotion[user_emotion])
else:
    print("i am sorry, i don't understand that emotion") 
"""
#prompt student aabout their mental health
response = input("How are you feeling today?(good /bad):")
if response.lower()=="good":
    print ("great keep it up")
elif response.lower() == "bad":
    print("am sorry to hear that ")
else:
    print('invalid response')         

    