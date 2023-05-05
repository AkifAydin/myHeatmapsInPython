import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
# this for the rows and columns
data = pd.read_csv("heatmap_dataset_1.csv", sep=";", decimal=',')
# this is for the data as float (else String making problems)
data2 = pd.read_csv("heatmap_dataset_1.csv", sep=";", index_col=0, decimal=',')

# Define row and column labels
header = data.columns[1:].tolist()  # only first column
header.reverse()  # reverse it bcs I want to have M1 and M1 both on the bottom left to start
print(header)
index = data.iloc[:, 0].tolist()  # only first row
print(index)

# create sample matrix reverse it bcs I want to have M1 and M1 both on the bottom left to start
sample_matrix = data2.values.astype(float)[::-1]
print(sample_matrix)

#cmap farben:
# jet
# viridis
# inferno
# magma
# plasma

# Create heatmap
# cmap = color name + s
# annot = Values in the fields to be shown or not
# fmt = shows 1 decimal places (in detail is the format Type of the String)
# cbar = corrulation bar
# xticklabels = xField
# yticklabels = yField
sns.heatmap(sample_matrix, cmap="jet", annot=False, fmt=".1f", cbar=True, xticklabels=index, yticklabels=header, linewidths=0.5, linecolor="yellow")

# Set axis labels and title
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.title("Heatmap Correlation")

# Adjust bottom and top spacing
plt.subplots_adjust(bottom=0.18, top=0.9)

# Show the plot
plt.show()
