import random

# Create a list with 10 numbers and 4 letters
lottery_pool = list(range(1, 11)) + ['A', 'B', 'C', 'D']

# Shuffle the list
random.shuffle(lottery_pool)

print("Lottery Pool (shuffled):")
print(lottery_pool)

# Pick 4 random lottery winners
print("\n4 Random Lottery Winners:")
winners = random.sample(lottery_pool, 4)
for i, winner in enumerate(winners, 1):
    print(f"Winner {i}: {winner}")

    print("\nAny ticket with this number/letter wins a prize!")