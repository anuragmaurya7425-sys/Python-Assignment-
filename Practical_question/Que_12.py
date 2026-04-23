# Write a program to demonstrate list slicing and list manipulation.

numbers = [10, 20, 30, 40, 50, 60, 70]

# list slicing
print("original:", numbers)
print("first three:", numbers[:3])
print("last three:", numbers[-3:])
print("every second element:", numbers[::2])

# list manipulation
numbers.append(80)
numbers.insert(2, 25)
numbers.remove(40)
popped = numbers.pop()
numbers[1] = 15

print("after append, insert, remove, pop, assign:", numbers)
print("popped value:", popped)

# sort and reverse
numbers.sort(reverse=True)
print("sorted descending:", numbers)
numbers.reverse()
print("reversed:", numbers)