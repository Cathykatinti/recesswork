from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import font
root=Tk()
root.title()
root.iconbitmap()
root.geometry()


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation.get() == "Add(+)":
            result = num1 + num2
        elif operation.get() == "Subtract(-)":
            result = num1 - num2
        elif operation.get() == "Multiply(*)":
            result = num1 * num2
        elif operation.get() == "Divide(/)":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = ""
#diplays the result from the calculate() function   
    
        label_result.config(text="Result: " + str(result))
        
    except ValueError:
        label_result.config(text="Invalid input")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result:")
# Create the main window
window = tk.Tk()
window.title("Catherine Natukunda")

# Create and place the input fields and labels
#entry_num1 and entry_num2 created to input the numbers
#packed by the pack() method to place them in the window
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()
#created to indicate the operation selection
label_operation = tk.Label(window, text="Select Operation:")
label_operation.pack()

# Create and place the operation selection radio buttons
operation = tk.StringVar()
operation.set("Add")  # Set default operation to Add

radio_add = tk.Radiobutton(window, text="Add(+)", variable=operation, value="Add(+)")
radio_add.pack()

radio_subtract = tk.Radiobutton(window, text="Subtract(-)", variable=operation, value="Subtract(-)")
radio_subtract.pack()

radio_multiply = tk.Radiobutton(window, text="Multiply(*)", variable=operation, value="Multiply(*)")
radio_multiply.pack()

radio_divide = tk.Radiobutton(window, text="Divide(/)", variable=operation, value="Divide(/)")
radio_divide.pack()

# Create and place the calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

button_clear = tk.Button(window, text="Clear", command=clear)
button_clear.pack()

#button_result = tk.Button(Window,text = "Result",command=Result)
#button_result.pack()
# Create and place the result label to display 
label_result = tk.Button(window, text="Result:")
label_result.pack()

# Start the Tkinter event loop
window.mainloop()
