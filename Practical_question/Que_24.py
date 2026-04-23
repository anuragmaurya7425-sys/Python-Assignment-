# Write a program to handle exceptions using try-except blocks.

try:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    result = num1 / num2 
    print(f"Result is :{result}")

except ZeroDivisionError:
    print("Error : You can not devided by Zero")

finally:
    print("Program executed completelly!")