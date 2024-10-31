import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

window = Tk()
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
                    id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
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

    product_exists = cur.execute("SELECT * FROM productstb WHERE name = ?", (name,)).fetchone()
    if product_exists:
        messagebox.showinfo("Alert!", "Product already exists. Update product.")
        return
    
    cur.execute("INSERT INTO productstb (name, description, quantity, price) VALUES (?, ?, ?, ?)", 
                (name, description, quantity, price))
    con.commit()
    messagebox.showinfo("Confirmation", "Item added successfully.")


def update_product():
    description = description_var.get()
    quantity = quantity_var.get()
    price = price_var.get()
    
    cur.execute("UPDATE productstb SET description = ?, quantity = ?, price = ? WHERE name = ?", 
                (description, quantity, price, id))
    con.commit()
def products_number():
    cur.execute("SELECT COUNT(*) FROM productstb")
    count = cur.fetchone()[0]
    total_products.config(text=f"Total Products: {count}")

def delete_product():
    name = name_var.get()
    cur.execute("DELETE FROM productstb WHERE name = ?", (name,))
    con.commit()

def product_information():
    display_products.delete("1.0", "end")
    cur.execute("SELECT * FROM productstb")
    products = cur.fetchall()
    for product in products:
        display_products.insert("end", f"{product[0]}: {product[1]} - {product[2]}Kg, Qty: {product[3]}, Price: R{product[4]:.2f}\n")

name_var = StringVar()
Entry(window, textvariable=name_var).grid(row=0, column=1)
Label(window, text="Name: ").grid(row=0, column=0)

description_var = StringVar()
Entry(window, textvariable=description_var).grid(row=1, column=1)
Label(window, text="Description: ").grid(row=1, column=0)

quantity_var = StringVar()
Entry(window, textvariable=quantity_var).grid(row=2, column=1)
Label(window, text="Quantity: ").grid(row=2, column=0)

price_var = StringVar()
Entry(window, textvariable=price_var).grid(row=3, column=1)
Label(window, text="Price: ").grid(row=3, column=0)

Button(window, text="Add Product", command=add_product).grid(row=4, column=0)
Button(window, text="Update Product", command=update_product).grid(row=4, column=1)
Button(window, text="Delete Product", command=delete_product).grid(row=4, column=2)

display_products = Text(window, height=10, width=50)
display_products.grid(row=5, column=0, columnspan=5)

scrollbar = Scrollbar(window, command=display_products.yview)
scrollbar.grid(row=5, column=5, sticky="ns")
display_products["yscrollcommand"] = scrollbar.set

sort_options = ["Name", "Price", "Quantity"]
sort_combobox = ttk.Combobox(window, values=sort_options)
sort_combobox.grid(row=6, column=0)
Button(window, text="Sort").grid(row=6, column=1)

total_products = Label(window, text=f"Total Products: ")
total_products.grid(row=7, column=0)

window.mainloop()
