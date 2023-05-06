import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Read CSV file
data = pd.read_csv("heatmap_dataset_1.csv", sep=";", decimal=',')
data2 = pd.read_csv("heatmap_dataset_1.csv", sep=";", index_col=0, decimal=',')

# Define row and column labels
header = data.columns[1:].tolist()
header.reverse()
print(header)
index = data.iloc[:, 0].tolist()
print(index)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid of x,y values
x, y = np.meshgrid(range(len(header)), range(len(index)))

# Interpolate z-values from data
z = griddata((x.flatten(), y.flatten()), data2.iloc[:, 0:].values.flatten(), (x, y), method='cubic')

# Create color map
cm = plt.get_cmap('plasma')

# Plot 3D heatmap
ax.plot_surface(x, y, z, cmap=cm)

# Set axis labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show plot
plt.show()
