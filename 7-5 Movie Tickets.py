print("Welcome to the movie theater!")

tickets = int(input("How many tickets would you like to purchase? "))

total_cost = 0

for i in range(tickets):
    age = int(input(f"Enter the age of person {i + 1}: "))
    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10.")
        total_cost += 10
    else:
        print("Your ticket is $15.")
        total_cost += 15

# final cost
print(f"The total cost for {tickets} tickets is: ${total_cost}")

