import matplotlib.pyplot as plt
import numpy as np

try:
    # Take user input from command line
    probability_percent = float(input("Enter probability of pulling Kageyama (in %): "))
    p = probability_percent / 100  # convert to decimal

    if not (0 < p < 1):
        raise ValueError("Probability must be between 0 and 100")

    x = np.linspace(0, 100, 101)
    y = 1 - (1 - p) ** x

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)
    plt.xticks(np.arange(0, 101, 10))
    plt.xlabel('number of pulls')
    plt.ylabel('probability of pulling at least one kageyama')
    plt.title('Cumulative Probability of Monster Acquisition per Number of Pulls')
    plt.grid(True)
    plt.savefig("gacha_chart.png")
    plt.show()

except ValueError as e:
    print(f"Invalid input: {e}")