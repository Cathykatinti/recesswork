"""
#inherintance
class Person:
   def __init__(self,name,age) 
    self.name=Name
    self.age=age

  def eat  (self)
     print(f"{self.name}is a is a person's name")
  


class Student(Person):
    print(f"{self.age}is the age of that person")
    print(f"{self.name}is the oldest ")

myperson = Person()    

#example2
class Vehicle:
    def__iit__(self,brand,color):
      self.brand = brand
      self.color = color

    def  display(veh):
        print(f"{self.name} is good")

class Car(Vehicle):
    def__init__(self,brand,color,wheel):
    super.__init__(brand,color)
    self.wheel = 4

     def move(self)
     print(f"{self.wheel}are for normal vehicles")

    mycar = Car("Benz","Blue")  
    mycar.display()
    mycar.move()
    #ex1
    #demonstrate using inheritance to calculate area and perimeter of a circle and rectangle respectively
class Shape:
    def __init__(self ,width,radius):
      self.length =width
      self.radius = radius

class Circle(Shape):
    def __init__(self):   
      Shape.__init__(self,width,radius)

    def area(self):
        return 3.4*self.radius

class Rectangle(Shape):
    def __init__(self,length):
      super.__init__(self,width,radius)

    def perimeter(self):
            return 2*(self.lenght+self.width)

    x = Circle(5)
    x.area() 
    y = Rectangle(10,8) 
    y.perimeter()  
    #example 3
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Flyable:
    def fly(self):
        print(f"{self.name}")
class Bird(Animal,Flyable):    
    def __init__(self,name,species):
        super().__init__(name) 
        self.species = species

    def display(self):
        super().display()         
        print(F"species:{self.species}") 
        print(f"name:{self.name}")

mybird = Bird("pigeon","parrot")  
mybird.eat() 
mybird.fly()   
#mybird.display()  
#method overriding using method inheritance
class Animal:
    def make_sound(self):
        print("Animal is making a sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
class Cat(Animal):
    def make_sound(self):
        print("Cat is meawing")   
    def make_sound(Animal):
        animal.make_sound()
        #make_animal_sound()
        #object
animal = Animal()
dog = Dog()
cat = Cat()      
Animal.make_sound(animal)
Dog.make_sound(dog)
Cat.make_sound(cat)
#make_aniaml_sound(dog)
#make_animal_sound(cat)           

#Polymorphism allows u to write code that can work diff objects
class Shape:
  def calculate_area(self):
    pass
class Rectangle(Shape):
   def __init__(self ,lenght,width):
     self.lenght = lenght
     self.width = width

   def calculate_area(self):
        return self.lenght*self.width

class Circle(Shape):
    def __init__(self ,radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14*self.radius**2 #radius*radius
    def calculate_circumference(self):              
        return 2*3.14*self.radius
my_rectangle = Rectangle(5,5)
my_circle = Circle(5)
#implementation
print("area of a rectangle:",my_rectangle.calculate_area())
print("circle area:",my_circle.calculate_area())

#overloading
class Calculator:
    def add(self,a,b):
     return a+b

    def add(self,a,b,y): 
        return a+b+y

my_calc = Calculator()
#print(my_calc.add(1,2))   
#overloading in python is kinda impossible with tradition son it takes the last one 
print(my_calc.add(1,2,3))
#abstraction allow u focus on essential features and hide them from 
from abc import ABC,
class Vehicle(ABC):
    def start(self):
       pass
    def  stop(self):
        print("stopping the car")  
class Car(Vehicle):

    car.start()
    truck.start()

    truck.stop()
    car.stop()  """      
    #demonstarte abstraction using calculating area of a circle
import math
from abc import ABC
class Shape:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pass    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
    def get_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__(radius)
        self.length = length 

    def get_perimeter(self):
        return 2*self.width + self.length    

# Usage
radius = 5
circle = Circle(radius)
area = circle.get_area()
rectangle = Rectangle(10,2)
perimeter=rectangle.get_perimeter()

print(f"The area of the circle with radius {radius} is: {area}")
print(f"The perimeter of the rectangle: {perimeter}")
