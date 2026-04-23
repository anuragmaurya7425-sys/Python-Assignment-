# Write a program to demonstrate file pointer operations using seek().

# create and write data first
with open("text.txt", "w") as f:
    f.write("Hello Python Programming")

# open file for reading
with open("text.txt", "r") as f:
    print("Initial position:", f.tell())   # pointer at start

    print("Read 5 characters:", f.read(5))
    print("Position after reading 5 chars:", f.tell())

    f.seek(6)
    print("Position after seek(6):", f.tell())

    print("Reading from position 6:", f.read())