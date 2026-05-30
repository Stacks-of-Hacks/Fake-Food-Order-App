# WARNING: THIS APP DOES NOT ORDER REAL FOOD OR ANY ITEMS. THIS IS A SIMULATION FOR MY LEARNING PURPOSES ONLY SO DON'T SUE ME.
# also this app was not made by ai
import json
import os

items = []
# this is the menu
menu = {
    "Burgers": {
        "Classic Burger": 9.99,
        "Cheese Burger": 10.99,
        "Double Burger": 12.99
    },
    "Sides": {
        "Fries": 3.99,
        "Onion Rings": 4.99,
        "Coleslaw": 2.99
    },
    "Drinks": {
        "Soda": 2.49,
        "Water": 1.99,
        "Coffee": 3.99
    }
}

# File path for saving orders
ORDER_FILE = "order.json"

# Load existing order if it exists
if os.path.exists(ORDER_FILE):
    with open(ORDER_FILE, "r") as f:
        items = json.load(f)

print(items)

def save_order():
    with open(ORDER_FILE, "w") as f:
        json.dump(items, f)

def add_item():
    # Display available categories
    print("Available categories:", ", ".join(menu.keys()))
    category = input("What category? ").strip()
    
    if category not in menu:
        print("ERROR: That category doesn't exist.")
        return
    
    # Display items in that category
    print(f"Available {category}:", ", ".join(menu[category].keys()))
    ItemToAdd = input("What item would you like to add? ").strip()
    
    if ItemToAdd not in menu[category]:
        print("ERROR: That item is not on the menu.")
        return
    
    items.append(ItemToAdd)
    save_order()

def remove_item():
    ItemToRemove = input("What item would you like to remove? ")
    if ItemToRemove in items:
        items.remove(ItemToRemove)
        save_order()
    else:
        print("Nope that item is not in your list, do better.")

# just read the code (if you can't read, learn to read)
while True:
    userchoice = input("What would you like to do? ")
    if userchoice == "add":
        add_item()
        print(items)
    elif userchoice == "remove":
        remove_item()
        print(items)
    elif userchoice == "exit":
        print("Exiting ...")
        exit()
    else:
        print("ERROR: Invalid command")