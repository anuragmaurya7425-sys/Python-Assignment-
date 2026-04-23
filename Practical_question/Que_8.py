# Write a program using while loop to compute sum of first N natural numbers.

n = int(input("Enter N: "))
total = 0
i = 1

while i <= n:
    total += i
    print(i , end=" + ")
    i += 1
print(f"\nSum of first {n} natural numbers is {total}") 