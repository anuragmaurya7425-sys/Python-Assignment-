# Write a program to read contents of a file using read(), readline(), and readlines().

# Using read() - reads entire file as a single string
print("***************** Read lines ****************")
with open("Text.txt" , "r") as f:
    content = f.read()
    print(content)
    print()

# Using readline() - reads one line at a time
print("Using readline():")
with open('Text.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip())
    print(line2.strip())
    print()

# Using readlines() - reads all lines as a list
print("Using readlines():")
with open('Text.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())