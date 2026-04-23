#  Write a program using matplotlib to plot line and bar graphs.

import matplotlib.pyplot as plt

# Sample data
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 78, 92]

# ---------------- LINE GRAPH ----------------
plt.figure()

plt.plot(subjects, marks, marker='o')
plt.title("Student Marks (Line Graph)")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# ---------------- BAR GRAPH ----------------
plt.figure()

plt.bar(subjects, marks)
plt.title("Student Marks (Bar Graph)")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()