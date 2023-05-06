import plotly.graph_objs as go
import pandas as pd

# Read in the data from the CSV file
data = pd.read_csv("heatmap_dataset_1.csv", delimiter=';', decimal=',')

# Create the x, y, and z arrays for the heatmap
x = data.columns[1:]
y = data.iloc[:, 0]
z = data.iloc[:, 1:].values

# Define the trace for the heatmap
trace = go.Heatmap(x=x, y=y, z=z, colorscale="Reds")

# Define the layout for the plot
layout = go.Layout(
    title='3D Heatmap',
    scene=dict(
        xaxis=dict(title=x[0]),
        yaxis=dict(title=y.name),
        zaxis=dict(title='Values')
    )
)

# Create the plot figure and add the heatmap trace
fig = go.Figure(data=[trace], layout=layout)

# Show the plot
fig.show()
