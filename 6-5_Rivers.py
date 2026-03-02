# Dictionary of rivers and their locations
rivers={
    "French Broad": "United States",
    "Amazon": "South America",
    "Nile": "Africa,"
    }
# For loop to print the river and its location
for river, location in rivers.items():
    print(f"The {river} runs through {location}.")
# For loop to print the names of the rivers
print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(f"- {river}")
# For loop to print the locations of the rivers
print("\nThe following locations are included in the dictionary:")
for location in rivers.values():
    print(f"- {location}")