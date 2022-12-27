import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# Local
from plot_generator import plot_line
from plot_generator import plot_scatter
from plot_generator import plot_bar
from plot_generator import plot_heatmap

# Line Plot
data = { 5:5, 10:15, 15:25, 20:35, 25:45 }
plot_line("plot_line Test", list(data.keys()), list(data.values()), "x", "y", False)

# Scatter Plot
data = { 5:5, 10:15, 15:25, 20:35, 25:45 }
labels = [ "55", "1015", "1525", "2035", "2545" ]
plot_scatter("plot_scatter Test", list(data.keys()), list(data.values()), "x", "y", False, plabel=labels)

# Bar Plot
data = { 5:5, 10:15, 15:25, 20:35, 25:45 }
plot_bar("plot_bar Test", list(data.keys()), list(data.values()), "x", "y", False)

# Heatmap Plot
data = { 0:0, 1:1, 2:2 }
z = [ [0,1,2], [1,2,3], [2,3,4] ]
plot_heatmap("plot_heatmap Test", list(data.keys()), list(data.values()), z, "x", "y", "z")

print("\nSuccess!")
