# Deli Sandwiches
sandwich_orders = ['grilled cheese', 'turkey', 'club', 'veggie']
finished_sandwiches = []

# Simulate making each sandwich until there are no more orders left
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

