
# Part B - Shopping List Manager

# Start with an empty list
shopping_list = []

# Display the menu repeatedly
while True:
    print("\n--- SHOPPING LIST MANAGER ---")
    print("add / remove / show / done")

    choice = input("Enter your choice: ").lower()

    # Add an item
    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "has been added to your list.")

    # Remove an item
    elif choice == "remove":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    # Show all items
    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    # Exit the program
    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Please enter add, remove, show, or done.")
