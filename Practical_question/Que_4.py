# Find largest of three numbers 

a = int(input("Enter 1sr numbers :"))
b = int(input("Enter 2nd numbers :"))
c = int(input("Enter 3rd numbers :"))

if (a > b and a > c):
    print(f"\nLargest number is :{a}")
    
elif(b > a and b > c):
    print(f"\nLargest number is :{b}")
    
else:
    print(f"\nLargest number is :{c}")