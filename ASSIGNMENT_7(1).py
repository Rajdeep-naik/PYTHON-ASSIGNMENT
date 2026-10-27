import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

print(df.head())

plt.figure(figsize=(8,5))
plt.plot(df.index[:30], df["sepal length (cm)"][:30], marker='o',)
plt.title('line plot - sepal length')
plt.xlabel('data index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="species",y="sepal length (cm)")
plt.title('bar plot - sepal length by species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="species",y="sepal width (cm)")
plt.title('bar plot - sepal width by species')
plt.xlabel('Species')
plt.ylabel('Average Sepal length (cm)')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x="sepal length (cm)",y="sepal width (cm)",hue="species")
plt.title('scatter plot - sepal length vs sepal width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

plt.figure(figsize=(8,5))
correlation=df.select_dtypes(include="number").corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title('heatmap - correlation matrix')
plt.show()