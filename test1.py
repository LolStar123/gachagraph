import matplotlib.pyplot as plt
import numpy as np
from math import comb
import itertools

# Compute multinomial coefficient
def multinomial_coeff(counts):
    n = sum(counts)
    result = 1
    for c in counts:
        result *= comb(n, c)
        n -= c
    return result

# Compute joint probability: P(all X_i >= k_i)
def joint_at_least_k(n, probs, counts):
    m = len(probs)
    total_prob = 0

    if sum(probs) > 1:
        raise ValueError("Total probability exceeds 1")

    # Generate all possible outcomes where sum(allocations) <= n
    for allocation in itertools.product(range(n + 1), repeat=m):
        if sum(allocation) > n:
            continue
        if all(allocation[i] >= counts[i] for i in range(m)):
            r = n - sum(allocation)
            coeff = multinomial_coeff(list(allocation) + [r])
            prob = coeff
            for i in range(m):
                prob *= (probs[i] ** allocation[i])
            prob *= (1 - sum(probs)) ** r
            total_prob += prob

    return total_prob

# === Input loop ===
probs = []
counts = []

for i in range(5):
    p = float(input(f"Enter probability of pulling Monster {i+1} (in %, or 0 to stop): ")) / 100
    if p == 0:
        break
    k = int(input(f"How many of Monster {i+1} do you want? (0 to stop): "))
    if k == 0:
        break
    probs.append(p)
    counts.append(k)

if len(probs) == 0:
    print("No valid monster data provided.")
else:
    x = np.arange(0, 101)
    y = [joint_at_least_k(n, probs, counts) if n >= sum(counts) else 0 for n in x]

    label_text = ' AND '.join([f'≥{counts[i]} of Mon{i+1}' for i in range(len(probs))])

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)
    plt.xticks(np.arange(0, 101, 10))
    plt.xlabel('number of pulls')
    plt.ylabel(f'P({label_text})')
    plt.title(f'Cumulative Probability of {label_text}')
    plt.grid(True)
    plt.savefig("gacha_multi_monster_chart.png")
    plt.show()
