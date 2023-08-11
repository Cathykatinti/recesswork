#we use try ,except and finally in handling exceptions
#two types of error in python that is Syntax error and exception
#errors are problems in a program due to which a program will stop the execution ,and they are caused when some internal events occur which change the normal flow of the program
"""in_bulit exception types
1.SyntaxError
2.TypeError
3.NameError
4.IndexError
5.KeyError
6.AttributeError
7valueError
8.ZeroDivisionError
9.IOError
10.ImportError
NB Syntaxerror is caused by wrong syntax and leads to termination of the program
while Exceptions areraised when the program is syntactically correct but the code results in erorr ,it doesnt stop execution pof the program but changes its normal flow
etc"""
#syntax error
"""class names
    def __init__(self):
        print("there is synatx error due to the wromg syntax in defining a class(:)was missed")
        """
#exceptions
num = int("abc")#this causes a value error because its trying to convert a non numeric string to an integer
#below is another example of exception(indexEror )as we try to access index that doesn'texist 
my_list = [1, 2, 3]
print(my_list[4])
#using try and except statements to catch and handle exceptions
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of the division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid operand types.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero error
divide_numbers("10", 2)  # Type error
#try with else statement
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        #the else block only exception
    else:
        print(f"The result of the division is: {result}")

# Usage
divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero error
#finally  keyword executes after the normal termination oth the try block
try:
    # Code block where an exception might occur
    numerator = 10
    denominator = int(input("Enter a number to divide numerator by: "))
    result = numerator / denominator
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input!")
    #the code in the finally block always executes regardless
finally:
    print("This block will always execute, regardless of exceptions.")



