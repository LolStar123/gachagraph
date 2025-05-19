import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(0, 100, 101) 

y = 1 - (0.98)**x

plt.figure(figsize=(8, 5))
plt.plot(x, y, linewidth=2)

plt.xticks(np.arange(0, 101, 10))

plt.xlabel('number of pulls')
plt.ylabel('probability of pulling at least at least one kageyama')

plt.title('Cumulative Probability of Monster Acquisition per Number of Pulls')
plt.grid(True)

plt.savefig("gacha_chart.png")
plt.show()