# Veriable assignment and swapping value

number1 = "Aditya Vishwakarma"  #string assignment
number2 = 25    #number assignment

#multiple assignment like 
num1 , num2 , num3 = 2, 3, 5
print(num1 , num2 ,num3)

# Swapping in python is easier way to swap two numbers
x = 5
y = 3
print(f"Before swapping :{x,y}")

x , y = 3 , 5
print(f"After swapping :{x , y}")


# Swaping using third veriable 
a = 9
b = 8
print(f"Before Swappping :{a , b}")

temp = a
a = b
b = temp
print(f"After swapping :{a , b}")


# Arithmetic swappping without using third veriable
c = 6
d = 7
print(f"Before swapping :{c , d}")

c = c + d
d = c - d 
c = c - d
print(f"After swapping :{c , d}")