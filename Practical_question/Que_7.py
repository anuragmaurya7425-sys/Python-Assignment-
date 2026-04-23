# Write a program to iterate through string, list, and dictionary using loops.

# string, list, and dictionary
my_string = "Hello, World!"
my_list = [1, 2, 3, 4, 5]
my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
        }

# Iterate through string
print("Iterating through string:")
for char in my_string:
    print(char, end=" ")
print("\n")

# Iterate through list
print("Iterating through list:")
for item in my_list:
    print(item, end=" ")
print("\n")

# Iterate through dictionary
print("Iterate through dictionary ")
for key , Value in my_dict.items():
    print(f"{key} : {Value}")