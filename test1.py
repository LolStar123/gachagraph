import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(0, 10, 100)  # from 0 to 10 pulls

# Example function y = 2x (placeholder)
y = 2 * x  # Replace this if you want real gacha logic

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, linewidth=2)

# Update axis labels
plt.xlabel('number of pulls')
plt.ylabel('probability of pulling at least one kageyama')

# Title and grid
plt.title('Line Chart of y = 2x')
plt.grid(True)

# Save to file
plt.savefig("gacha_chart.png")
plt.show()