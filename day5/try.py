import tkinter as tk
from tkinter import messagebox

class ReceiptPrintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing App")

        # Create labels and entry fields
        tk.Label(root, text="Customer_Name").grid(row=0, column=0, padx=10, pady=5)
        self.customer_entry = tk.Entry(root)
        self.customer_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Item").grid(row=0, column=0, padx=10, pady=5)
        self.item_entry = tk.Entry(root)
        self.item_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Price").grid(row=1, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create buttons
        self.add_button = tk.Button(root, text="customer_name", command=self.add_item)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add_Item", command=self.add_item)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.print_button = tk.Button(root, text="Print_Receipt", command=self.print_receipt)
        self.print_button.grid(row=2, column=1, padx=10, pady=5)

        # Create a text widget to display the receipt
        self.receipt_text = tk.Text(root, width=40, height=10)
        self.receipt_text.grid(row=3, columnspan=2, padx=10, pady=5)

        # Initialize an empty receipt
        self.receipt = []

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        customer_name=self.customer_entry.get()

        if item and price:
            self.receipt.append((item, price))
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both item and price.")

    def print_receipt(self):
        self.receipt_text.delete(1.0, tk.END)

        if len(self.receipt) == 0:
            messagebox.showerror("Error", "No items in the receipt.")
            return

        total = 0
        for item, price, in self.receipt:
            self.receipt_text.insert(tk.END, f"{item}: ${price}\n")
            total += float(price)

        self.receipt_text.insert(tk.END, "----------------------\n")
        self.receipt_text.insert(tk.END, f"Total: ${total}")

        # Additional actions for a boss to accept
        # Here, you can include code to send the receipt to a printer or store it in a database, for example.
        # You can also format the receipt in a specific way to meet your boss's requirements.

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptPrintingApp(root)
    root.mainloop()
