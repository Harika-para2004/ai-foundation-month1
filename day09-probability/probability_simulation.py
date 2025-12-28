import random

print("Simulating 1000 coin tosses...")
tosses = [random.choice([0, 1]) for _ in range(1000)]   # 0 for tails, 1 for heads
heads = sum(tosses)
probability_heads = heads/len(tosses)
print("Estimated Probability of Heads: ", probability_heads)

print("\nSimulating 1000 rolls of a six-sided die...")
rolls = [random.randint(1,6) for _ in range(1000)]
for side in range(1,7):
    count = rolls.count(side)
    probability_side = count/ len(rolls)
    print(f"Estimated Probability of rolling a {side}: {probability_side}")

print("\nSimulating drawing 1000 cards from a standard deck...")
