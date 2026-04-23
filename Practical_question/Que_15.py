# Write a program using built-in functions on list, string, and dictionary.

# list built-in functions
numbers = [3, 1, 4, 1, 5, 9]

print("List:", numbers)
print("length:", len(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sum:", sum(numbers))
print("sorted:", sorted(numbers))
print("reversed:", list(reversed(numbers)))

print()     #for new line

# string built-in functions
text = "Adity Vishwakarma"
print("length:", len(text))
print("upper:", text.upper())
print("lower:", text.lower())
print("replace:", text.replace("Adity", "Aditya"))
print("split:", text.split())
print("join:", "-".join(text.split()))
print("count of l:", text.count("l"))
print("ends with Vishwakarma:", text.endswith("Vishwakarma"))

print()

# dictionary built-in functions
person = {"name": "Aditya", "age": 20, "city": "Mau"}
print("Dictionary:", person)
print("keys:", list(person.keys()))
print("values:", list(person.values()))
print("items:", list(person.items()))
print("length:", len(person))
print("get age:", person.get("age"))
print("get country with default:", person.get("country", "Unknown"))

# build a dictionary from two lists
keys = ["apple", "banana", "cherry"]
values = [3, 5, 2]
fruit_counts = dict(zip(keys, values))
print("Built from lists:", fruit_counts)