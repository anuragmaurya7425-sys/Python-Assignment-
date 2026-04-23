#  Write a program using pandas to filter and group data

import pandas as pd

# Read CSV file
df = pd.read_csv("student.csv")

print("Original Data:\n", df)

# FILTERING
print("\nStudent with marks > 80:")
high_marks = df[df['marks'] > 80]
print(high_marks)

print("\nStudent from BCA course:")
bca_students = df[df['course'] == "BCA"]
print(bca_students)

# GROUPING
print("\nAverage marks by course:")
grouped = df.groupby('course')['marks'].mean()
print(grouped)

print("\nMaximum marks by course:")
grouped_max = df.groupby('course')['marks'].max()
print(grouped_max)