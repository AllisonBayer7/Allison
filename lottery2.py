import random

# Create a list with 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

# Randomly select four numbers and one letter
lottery_numbers = random.sample([1,2,3,4,5,6,7,8,9,10], 4)
lottery_letter = random.choice(['A', 'B', 'C', 'D', 'E'])

# Combine into a single lottery code
lottery_code = "".join(str(num) for num in lottery_numbers) + lottery_letter

print(f"\nLottery number generated: {lottery_code}")

# Get user input
user_code = input("Enter your lottery number (4 numbers + 1 letter): ")

# Compare and print result
if user_code == lottery_code:
    print("🎉 Congratulations! You are a WINNER!")
else:
    print("Sorry, that is not the winning number. Better luck next time!")