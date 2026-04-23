# Write functions to organize a program that performs basic operations on strings and lists.

# length of string
def length(s):
    return len(s)

# reverse string
def reverse(s):
    return s[::-1]

# convert to uppercase
def upper(s):
    return s.upper()

# sum of list
def total(lst):
    return sum(lst)

# maximum element
def maximum(lst):
    return max(lst)

# reverse list
def reverse_list(lst):
    return lst[::-1]

# string input
s = input("Enter string: ")
print("Length:", length(s))
print("Reverse:", reverse(s))
print("Upper:", upper(s))

# list input
lst = list(map(int, input("Enter numbers: ").split()))
print("Sum:", total(lst))
print("Max:", maximum(lst))
print("Reverse list:", reverse_list(lst))