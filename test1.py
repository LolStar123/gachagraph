import matplotlib.pyplot as plt
import numpy as np
from math import comb

def joint_at_least_k_monsters(n, p1, k1, p2, k2):
    if p1 + p2 > 1:
        raise ValueError("The sum of probabilities for monster 1 and 2 must be ≤ 1.")

    total_prob = 0

    # Iterate over all possible counts of monster 1 (x) and monster 2 (y)
    for x in range(n + 1):
        for y in range(n - x + 1):
            r = n - x - y
            # Only include if it satisfies at least k1 of mon1 AND at least k2 of mon2
            if x >= k1 and y >= k2:
                multinom_coeff = comb(n, x) * comb(n - x, y)  # multinomial coeff: C(n, x) * C(n-x, y)
                prob = multinom_coeff * (p1 ** x) * (p2 ** y) * ((1 - p1 - p2) ** r)
                total_prob += prob

    return total_prob

try:
    # === User Inputs ===
    p1 = float(input("Enter probability of pulling Monster 1 (in %): ")) / 100
    k1 = int(input("How many of Monster 1 do you want? "))

    p2 = float(input("Enter probability of pulling Monster 2 (in %): ")) / 100
    k2 = int(input("How many of Monster 2 do you want? "))

    if any(p <= 0 or p > 1 for p in (p1, p2)):
        raise ValueError("Probabilities must be between 0 and 100%")
    if p1 + p2 > 1:
        raise ValueError("Sum of monster probabilities must be ≤ 100%")
    if k1 < 1 or k2 < 1:
        raise ValueError("You must want at least one of each monster")

    x = np.arange(0, 101)
    y = [joint_at_least_k_monsters(n, p1, k1, p2, k2) if n >= (k1 + k2) else 0 for n in x]

    # === Plotting ===
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)
    plt.xticks(np.arange(0, 101, 10))
    plt.xlabel('number of pulls')
    plt.ylabel(f'P(≥{k1} Mon1 AND ≥{k2} Mon2)')
    plt.title(f'Cumulative Probability of Getting ≥{k1} Mon1 and ≥{k2} Mon2')
    plt.grid(True)
    plt.savefig("gacha_dual_monster_chart.png")
    plt.show()

except ValueError as e:
    print(f"Input error: {e}")
