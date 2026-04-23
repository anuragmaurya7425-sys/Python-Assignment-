# Write a program to write and append data to a file.

#read data
with open("Text.txt", "r") as f:
    result = f.read()
    print(result)

# append mode
with open("Text.txt", "a") as f:
    f.write("This line is added later.\n")

print("Data appended successfully")
