import matplotlib.pyplot as plt
import pandas as pd

# 1. Take file name from user
file_name = input("Enter file name: ")
df = pd.read_csv(file_name)

# 2. Calculate and print averages
print("Average Maths:", df["Maths"].mean())
print("Average Python:", df["Python"].mean())
print("Average Attendance:", df["Attendance"].mean())

# 3. Histogram of Python marks
plt.hist(df["Python"])
plt.title("Histogram of Python Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Box plot for Maths and Python
plt.boxplot([df["Maths"], df["Python"]])
plt.title("Box Plot of Maths and Python")
plt.xticks([1, 2], ["Maths", "Python"])
plt.ylabel("Marks")
plt.show()

# 5. Pie chart for Cities
counts = df["City"].value_counts()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
plt.title("Students by City")
plt.legend()
plt.show()