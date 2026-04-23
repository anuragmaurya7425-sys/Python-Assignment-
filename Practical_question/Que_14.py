# Write a program to perform dictionary operations (add, update, delete).

def show_menu():
    print("\nDictionary Operations")
    print("1. Add item")
    print("2. Update item")
    print("3. Delete item")
    print("4. Show dictionary")
    print("5. Exit")


def add_item(d):
    key = input("Enter key to add: ")
    if key in d:
        print("Key already exists. Use update instead.")
    else:
        value = input("Enter value: ")
        d[key] = value
        print(f"Added: {key} -> {value}")


def update_item(d):
    key = input("Enter key to update: ")
    if key not in d:
        print("Key not found.")
    else:
        value = input("Enter new value: ")
        d[key] = value
        print(f"Updated: {key} -> {value}")


def delete_item(d):
    key = input("Enter key to delete: ")
    if key in d:
        del d[key]
        print(f"Deleted key: {key}")
    else:
        print("Key not found.")


def main():
    data = {}
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_item(data)
        elif choice == "2":
            update_item(data)
        elif choice == "3":
            delete_item(data)
        elif choice == "4":
            print("Current dictionary:", data)
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()