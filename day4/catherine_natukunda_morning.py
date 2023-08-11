"""class BankAccount:
    def display(self)
#create an account
my_account = BankAccount("123456789",100)
#perform operations
my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()
#caalculate a perimeter of rectangle
my_rectangle = rectangle(15,5)
print(my_rectangle.length)
print(my_rectangle.width)
#calculate and display the area
print(my_rectangle.calculate_area)
print(my_rectangle.calculate_parimeter)
#university
class Student:
    def __init__(self,name,year,course):
       self.name = Name
       self.year = year
       self.course = course

    def displaydetails(self):
        print("name:",self,name)
        print("year:",self,year)
        print("course:",self,course)
# create Student object
my_student = Student( "catherine Natukunda",3,"Software Engineering")        
# dispaly the student details
my_student.display_deatails()
#class initialisation
class Person:
    def __init__ (self,name,age):
      self.name
      self.age
    def greet(self):
       print("hellow ,my name ",self.name)
       print("i am",self.age,"years old")
#creating a person object
my_person = Person("cathy",23)       
    print(my_person.name)
    print(myperson.age)
#calculate the area and circumference of a circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return 2*3.14*self.radius
    def calculate circumference(self):
        return 2*3.14*self.radius 
        my_circle = Circle(7)
        print(my_circle.radius)     
        print(my_circle.radius)
        print(my_circle.calculate_area())
        print(my_circle.calculate_circumference())   
#calculate and display employee bonuses (15)of salary(employee = 150000,employee1 = 230000)            
employees = {
    "employee": 150000,
    "employee1": 230000,
}

bonus_percentage = 0.15  # 15% bonus

# Calculate and display bonuses
for employee, salary in employees.items():
    bonus = salary * bonus_percentage
    total_salary = salary + bonus
    print(f"{employee}: Salary = {salary}, Bonus = {bonus}, Total Salary = {total_salary}")"""
#Encapsulation
#key goals of encapsulation are
"""
1 to hide the implementation of details of an object
2 protect the object from external changes
protect the objects from changes
3organise code
class BankAccount:
  def __init__(self,account_number,balance):
#encapsulation    
    self._account_number = account_number
    self._balance = balance
  def deposit(self,amount):
    self._balance +=amount
  def withdraw(self,amount):
    if self._balance>=amount:
        self._balance-=amount
    else:
        print("insufficient")
  def get_balance(self):
     return self.balance
#create bankaccount object
my_account = BankAccount("1234567890",2000) 
print(my_account._account_number) 
print(my_account._balance)   
my_account.deposit(500) 
print(my_account._balance)
my_account.withdraw(100)
print(my_account._balnce)"""
#ex2 covert temp(37)from celsius to fahrenheit
class Temperature:
    #self parameter is areference to the current instance of the class and its ued to access variables that belong to that class,NB anyword can be used instead of self
    def __init__(mytry,celsius):
        #encapsulation using the underscore(_)
        mytry._celsius = celsius
    def convert_to_fahrenheit(mytry):
        mytry._fahrenheit = (mytry._celsius*9/5)+32
        return mytry._fahrenheit
    def get_celsius(mytry):
        return mytry._celsius
my_temp = Temperature(37)        
print(my_temp.get_celsius())
print(my_temp.convert_to_fahrenheit())
#assignment1
#show encapsulation with employee informations to give pay increamentation(salary with employee
# information to new salary)
"""class Employee:
 def __init__(self, employee_name="Ciara", salary=150000):
        self._employee_name=employee_name
        self._salary=salary
 def display(self):
        print(self._employee_name, "earns",self._salary)
 def calculate(self):

    if self._salary > 150000:
            print(self._salary*0.1)
            
    else:
            print(self._salary,"next month shift ,you will be worked on")

emp = Employee("cathy",1000000)
emp.display()
emp.calculate()
emp=Employee("Clare",600000)
emp.display()
emp.calculate()
emp = Employee("Benj",50000)
emp.display()
emp.calculate()
#for default initialization
emp=Employee()
emp.display()
emp.calculate()

#inheritance,polymorphism and abtraction
"""