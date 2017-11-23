#Create a Dictionary
#store = {"item": ["Footballs", "Basketballs", "Shorts", "Bats"], "qty":[20, 2, 80, 2]}
store = {"Footballs":20, "Basketballs": 2, "Shorts": 80, "Bat": 2}
#store = {"qty": {"Footballs":20, "Basketballs": 2, "Shorts": 80, "Bat": 2}}

#Prompt "If they would like to add a new item, remove, or display"

# answer = input("Would you like to add a new item? (y)es or (n)o")
# while (answer == "y"):
#     #Add which item and qty
#     item = input("Which item would you like to add?")
#     qty = input("How many?")
#     store[item] = int(qty)

#solution
manage_system = "y"
while manage_system == "y":
    action_item = input("Would you like to (A)dd, (R)emove an item, or (D)isplay store items")

    If action_item == "A":
        item_added = input("which item would you like to add?")
        qty_added = input("How many would you like to add?")
        store[item_added] = int(qty_added)
        #print confirmation
        print(item_added + " " + qty_added + "added!")

    elif action_item =="R":
        item_removed = input("which item would you like to remove?")
        if item_revoed in store: #does the item exist in ur current dictionary?
            #remove item
            del store(item_removed)
           
            #print confirmation
             print(item_removed + "removed!")
        else:
            print("the item does not exist")
    elif =="D"
        for key, value in store.items():
            print(key+ ": " + str(value))
    else:
        print("your input is not recognized.")

    manage_system = input("Would you like to continue working? (y)es or (n)o)")


    
