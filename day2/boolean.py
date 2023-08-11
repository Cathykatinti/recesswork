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
