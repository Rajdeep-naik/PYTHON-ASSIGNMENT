import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load the CSV file
df = pd.read_csv("sample_data_assignment_07.csv")

# 2. Display the data in terminal
print("Dataset:")
print(df)

# 3. Line Plot: Python marks of each student
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 4. Bar Plot: Maths marks of each student
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

# 5. Scatter Plot: Maths vs Python marks
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 6. Correlation Matrix and Heatmap
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("Correlation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()