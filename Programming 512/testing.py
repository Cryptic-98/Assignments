import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3


window = tk.Tk()
window.title("Inventory")
window.geometry("420x420")


icon = PhotoImage(file="inventory.png") 
window.iconphoto(True, icon)

def inventorydb():
    global con
    con = sqlite3.connect("inventory.db")
    global cur
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS productstb (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL);''')
    con.commit()


def add_product():
    inventorydb()
    name = name_var.get()
    description = description_var.get()
    quantity = quantity_var.get()
    price = price_var.get()

    if not name:
        messagebox.showerror("Error", "Name is required.")
        return
    elif not description:
        messagebox.showerror("Error", "Description is required.")
    elif not quantity:
        messagebox.showerror("Error", "Quantity is required.")
    elif not price:
        messagebox.showerror("Error", "Price is required.")
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer and Price must be a number.")
        return

    product_exists = cur.execute("SELECT * FROM productstb WHERE name = ?", (name,)).fetchone()
    if product_exists:
        messagebox.showinfo("Alert!", "Product already exists. Update the product.")
        return
    
    cur.execute("INSERT INTO productstb (name, description, quantity, price) VALUES (?, ?, ?, ?)", 
                (name, description, quantity, price))
    con.commit()
    messagebox.showinfo("Confirmation", "Item added successfully.")
    product_information()
    products_number()


def update_product():
    inventorydb()
    name = name_var.get()
    description = description_var.get()
    quantity = quantity_var.get()
    price = price_var.get()

    if not name:
        messagebox.showerror("Error", "Name field is required for updating.")
        return
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer and Price must be a number.")
        return
    cur.execute("UPDATE productstb SET description = ?, quantity = ?, price = ? WHERE name = ?", 
                (description, quantity, price, name))
    con.commit()
    messagebox.showinfo("Confirmation", "Item updated successfully.")
    product_information()

def delete_product():
    inventorydb()
    name = name_var.get()
    if not name:
        messagebox.showerror("Error", "Name field is required for deletion.")
        return
    cur.execute("DELETE FROM productstb WHERE name = ?", (name,))
    con.commit()
    messagebox.showinfo("Confirmation", "Item deleted successfully.")
    product_information()
    products_number()


def product_information():
    display_products.delete("1.0", "end")
    cur.execute("SELECT * FROM productstb")
    products = cur.fetchall()
    for product in products:
        display_products.insert("end", f"ID: {product[0]}\nName: {product[1]}\nDescription: {product[2]}Kg\nQty: {product[3]}\nPrice: R{product[4]:.2f}\n---------------------------------\n")


def products_number():
    cur.execute("SELECT COUNT(*) FROM productstb")
    count = cur.fetchone()[0]
    total_products.config(text=f"Total Products: {count}")


name_var = tk.StringVar()
tk.Entry(window, textvariable=name_var).grid(row=0, column=1)
tk.Label(window, text="Name: ").grid(row=0, column=0)

description_var = tk.StringVar()
tk.Entry(window, textvariable=description_var).grid(row=1, column=1)
tk.Label(window, text="Description: ").grid(row=1, column=0)

quantity_var = tk.StringVar()
tk.Entry(window, textvariable=quantity_var).grid(row=2, column=1)
tk.Label(window, text="Quantity: ").grid(row=2, column=0)

price_var = tk.StringVar()
tk.Entry(window, textvariable=price_var).grid(row=3, column=1)
tk.Label(window, text="Price: ").grid(row=3, column=0)


tk.Button(window, text="Add Product", command=add_product).grid(row=4, column=0)
tk.Button(window, text="Update Product", command=update_product).grid(row=4, column=1)
tk.Button(window, text="Delete Product", command=delete_product).grid(row=4, column=2)


display_products = tk.Text(window, height=10, width=50)
display_products.grid(row=5, column=0, columnspan=5)

scrollbar = tk.Scrollbar(window, command=display_products.yview)
scrollbar.grid(row=5, column=5, sticky="ns")
display_products["yscrollcommand"] = scrollbar.set


total_products = tk.Label(window, text=f"Total Products: ")
total_products.grid(row=7, column=0)


inventorydb()
product_information()
products_number()
window.mainloop()
