import tkinter as tk
from tkinter import messagebox

class Receipt:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def cust1(self):
        customer_name = 0
        for item1 in self.items:
           customer_name += item.get_customer_name()
        return customer_name

    def get_receipt_text(self):
        receipt_text = "Receipt: \n"
        for item in self.items:
            receipt_text += f"- {item.get_name()}: ${item.get_price()}\n"
        receipt_text += f"Total: ${self.calculate_total()}"
        return receipt_text


class Item:
    def __init__(self, name, price,customer_name):
        self.name = name
        self.price =float(price) 
        self.customer_name = customer_name

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

        
    def get_price(self):
        return self.customer_name


class ReceiptPrintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day_To_Day Supermarket_mbarara")

        # Create labels and entry fields
        tk.Label(root, text="customer_name").grid(row=0, column=0, padx=10, pady=5)
        self.customer_entry = tk.Entry(root)
        self.customer_entry.grid(row=0,column=1,padx=10,pady=5)
       # self.item_entry = tk.Entry(root)
        #self.item_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Item").grid(row=1, column=0, padx=10, pady=5)
        self.item_entry = tk.Entry(root)
        self.item_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Price").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create buttons
        #self.add_button = tk.Button(root, text="price", command=self.add_item)
        #self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=5)

        self.print_button = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=4, column=0, padx=10, pady=5)

        # Create a text widget to display the receipt
        self.receipt_text = tk.Text(root, width=40, height=10)
        self.receipt_text.grid(row=5, columnspan=2, padx=10, pady=5)

        # Initialize an empty receipt
        self.receipt = Receipt([])

    def add_item(self):
        customer_name = self.customer_entry.get()
        item = self.item_entry.get()
        price = self.price_entry.get()
        

        if item and price and customer_name:
            new_item = Item(item, float(price) ,customer_name)
            self.receipt.items.append(new_item)
           # self.receipt.customer_name.append(customer_name)
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.customer_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both item,price and customer_name.")

    def print_receipt(self):
        receipt_text = self.receipt.get_receipt_text()
        self.receipt_text.delete("1.0", tk.END)
        self.receipt_text.insert(tk.END, receipt_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptPrintingApp(root)
    root.mainloop()
