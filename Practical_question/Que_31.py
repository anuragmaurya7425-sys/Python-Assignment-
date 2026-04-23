#  Write a program combining numpy, pandas, and matplotlib for simple data analysis.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV using pandas
df = pd.read_csv("students.csv")

print("Original Data:\n", df)

# ---------------- NUMPY OPERATIONS ----------------
marks_array = np.array(df['marks'])

print("\nUsing NumPy:")
print("Average Marks:", np.mean(marks_array))
print("Maximum Marks:", np.max(marks_array))
print("Minimum Marks:", np.min(marks_array))

# ---------------- PANDAS ANALYSIS ----------------
print("\nUsing Pandas:")
print("Summary:\n", df.describe())

# Add new column (Grade)
df['grade'] = df['marks'].apply(lambda x: 'A' if x >= 85 else 'B')

print("\nData with Grades:\n", df)

# ---------------- FILTERING ----------------
high_scores = df[df['marks'] > 80]
print("\nStudents with marks > 80:\n", high_scores)

# ---------------- VISUALIZATION ----------------

# Line Graph
plt.figure()
plt.plot(df['name'], df['marks'], marker='o')
plt.title("Marks of Students (Line Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Graph
plt.figure()
plt.bar(df['name'], df['marks'])
plt.title("Marks of Students (Bar Graph)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()