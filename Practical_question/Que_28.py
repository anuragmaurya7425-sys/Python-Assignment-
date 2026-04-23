# Write a program using pandas to read a CSV file and perform basic analysis.

import pandas as pd

# Read CSV file
df = pd.read_csv("student.csv")

# Display data
print("Full Data:\n")
print(df)

# Basic Analysis
print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nColumn Names:")
print(df.columns)

print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Marks:")
print(df['marks'].mean())

print("\nMaximum Marks:")
print(df['marks'].max())

print("\nMinimum Marks:")
print(df['marks'].min())