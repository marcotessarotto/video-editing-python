# Importing packages
import matplotlib.pyplot as plt

# Define x and y values
x = [7, 14, 21, 28, 35, 42, 49]
y = [8, 13, 21, 30, 31, 44, 50]

# Plot a simple line chart without any feature
# supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(x, y, linestyle='-', linewidth=7, color='#0abab5')
#plt.show()

plt.plot([80, 20], [100, 100], 'r', linewidth=5)
plt.show()