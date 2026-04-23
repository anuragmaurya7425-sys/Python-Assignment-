# Write a program to copy contents of one file to another.

with open("Text.txt", "r") as f1:
    data = f1.read()
    print(data)
    
with open("CopyText.txt","w") as f2 :
    result = f2.write(data)
    print("Data copied successfully")