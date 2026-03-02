# Dictionary
favorite_places={
    'Hailey': ['Charelston', 'Savannah', 'New Orleans'],
    'Joe':['Baltimore', 'San Francisco', 'Nashville'],
    'Allison':['Key West', 'Savannah', 'New Orleans'],

} 
# For loop to print each person's favorite places
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")