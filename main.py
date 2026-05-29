# WARNING: THIS APP DOES NOT ORDER REAL FOOD OR ANY ITEMS. THIS IS A SIMULATION FOR MY LEARNING PURPOSES ONLY SO DON'T SUE ME.
# also this app was not made by ai
items = []
print(items)
def add_item():
    ItemToAdd = input("What item would you like to add? ")
    items.append(ItemToAdd)
def remove_item():
    ItemToRemove = input("What item would you like to remove? ")
    if ItemToRemove in items:
        items.remove(ItemToRemove)
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