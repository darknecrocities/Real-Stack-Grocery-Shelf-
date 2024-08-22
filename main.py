# Name:Parejas, Arron Kian M.
#      Marquez, Jian Kalel
#      Lumba, Nelwin

# View the entire shelf
def view_shelf(shelf):
    try:
        if shelf:
            # Iterate through each item and its stack
            for item, stack in shelf.items():
                if len(shelf[item]) != 0:
                    print("\nItem:", item)
                    print("--------------")
                    # Print items in the stack from top to bottom
                    for each in range(len(stack) - 1, -1, -1):
                        print("     ", item, "#" + str(each))
        else:
            print("\nShelf is empty!")
    except Exception as e:
        print(f"Error while viewing shelf: {e}")

# Push operation to add items to the shelf
def push(shelf):
    try:
        while True:
            # Input item name and ensure it is not empty
            item = input("\nItem: ").strip()
            if item:
                break
            print("Item cannot be empty. Please enter a valid item name.")

        while True:
            # Input amount and ensure it is a positive integer
            amount = input("Amount: ").strip()
            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                break
            print("Amount must be a positive integer. Please enter a valid amount.")

        # Non-Existing Item: Add new item to the shelf
        if item not in shelf.keys():
            if 0 < amount <= 10:
                shelf[item] = [item for _ in range(amount)]
            else:
                shelf[item] = [item for _ in range(10)]
        # Existing Item: Update the stack of an existing item
        else:
            counter = 0
            while counter < amount and len(shelf[item]) < 10:
                shelf[item].append(item)
                counter += 1

            if len(shelf[item]) == 10:
                print("Item:", item + "\nStack: Full")

    except Exception as e:
        print(f"Error while pushing stocks: {e}")

# Pop operation to remove items from the shelf
def pop(shelf):
    try:
        if shelf:
            print("\nItem bought")
            while True:
                # Input item name and ensure it exists in the shelf
                item = input("  - Item: ").strip()
                if item in shelf.keys():
                    break
                else:
                    print("Item not found. Try again.")

            while True:
                # Input amount and ensure it is valid
                amount = input("  - Amount: ").strip()
                if amount.isdigit() and 0 < int(amount) <= len(shelf[item]):
                    amount = int(amount)
                    break
                else:
                    print("Amount over the limit or invalid. Try again.")

            stop = len(shelf[item]) - amount
            print("\nItems removed:")
            # Remove items from the stack
            for i in range(len(shelf[item]) - 1, -1, -1):
                print(" ", shelf[item].pop() + " #" + str(i))
                if i == stop:
                    break

            warning(shelf)
            view_shelf(shelf)
        else:
            print("\nShelf is empty!\n")
            input("Press Enter to go back to the main menu")
    
    except Exception as e:
        print(f"Error while popping stocks: {e}")

# Display warnings for low stock or empty shelf
def warning(shelf):
    try:
        min_cap = 3
        for item in shelf.keys():
            if 0 < len(shelf[item]) <= 3:
                print("\nWARNING: Stock Low")
            elif len(shelf[item]) == 0:
                print("\nWARNING: No Stocks")
    except Exception as e:
        print(f"Error while checking warning: {e}")

# Main logic to run the menu and handle user actions
shelf = {}
main = True

print("\n\t  Welcome to the store!")

while main:
    try:
        print("\n------------- Main Menu -------------")
        print("\n\t  [1]\tView Shelf\n\t  [2]\tPush Stocks\n\t  [3]\tPop Stacks\n\t  [4]\tQuit")

        action = input("\nAction: ")

        match action:
            case "1":  # Viewing
                view_shelf(shelf)
                input("\nPress Enter to go back to the main menu")
            case "2":  # Adding / Pushing
                push(shelf)
                input("\nPress Enter to view shelf")
                view_shelf(shelf)
                input("\nPress Enter to go back to the main menu")
            case "3":  # Removing / Popping
                pop(shelf)
                input("\nPress Enter to go back to the main menu")
            case "4":  # Quit
                print("\nQuitting program\n")
                main = False
            case _:
                raise ValueError("Invalid input. Please enter a valid action number (1-4).")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
