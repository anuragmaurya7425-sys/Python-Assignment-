# Write a program to perform tuple operations and demonstrate immutability.

t = (1, 2, 3, 'a', 'b')

print("Original tuple:", t)
print("First element:", t[0])
print("Slice from index 1 to 3:", t[1:4])
print("Length:", len(t))
print("Concatenation:", t + ('c', 'd'))
print("Repetition:", t * 2)
print("Membership test for 'a':", 'a' in t)
print("Count of 2:", t.count(2))
print("Index of 'b':", t.index('b'))

try:
    t[0] = 10
except TypeError as e:
    print("Attempt to modify tuple element failed:", e)

# Demonstrate how to modify values by converting to a list and back
mutable_version = list(t)
mutable_version[0] = 10
t_modified = tuple(mutable_version)
print("Modified tuple via list conversion:", t_modified)