import matplotlib.pyplot as plt
import numpy as np
from math import comb

def cumulative_prob_at_least_k(n, p, k):
    # 1 - sum of probabilities from X = 0 to k-1
    return 1 - sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k))

try:
    # Input from user
    p_percent = float(input("Enter probability of pulling Kageyama (in %): "))
    k = int(input("Enter desired number of Kageyamas: "))
    
    p = p_percent / 100
    if not (0 < p < 1):
        raise ValueError("Probability must be between 0 and 100")
    if k < 1:
        raise ValueError("Number of Kageyamas must be at least 1")
    
    # Generate pulls from 0 to 100
    x = np.arange(0, 101)  # integer pulls only
    y = [cumulative_prob_at_least_k(n, p, k) if n >= k else 0 for n in x]

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)
    plt.xticks(np.arange(0, 101, 10))
    plt.xlabel('number of pulls')
    plt.ylabel(f'P(at least {k} Kageyama{"s" if k > 1 else ""})')
    plt.title(f'Cumulative Probability of Getting ≥{k} Kageyama{"s" if k > 1 else ""}')
    plt.grid(True)
    plt.savefig("gacha_chart.png")
    plt.show()

except ValueError as e:
    print(f"Input error: {e}")