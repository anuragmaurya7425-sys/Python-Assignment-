# Write a program using nested if to classify a number (positive,negative, zero).

num = int(input("Enter a number :"))

if( num >= 0):
    print("Number is positive")
    
    if(num == 0):
        print("Given number is zero")

else:
    print("Given number is nagative")