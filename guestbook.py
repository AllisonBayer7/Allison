print("Welcome to the Guest Book!")
print("Type 'quit' to stop.\n")

while True:
    name = input("Please enter your name: ")

    if name.lower() == 'quit':
        print("Goodbye!")
        break

    # Print greeting
    print(f"Hello, {name}! Thanks for visiting.")

    # Record visit in guest_book.txt
    with open("guest_book.txt", "a") as file:
        file.write(f"{name} visited.\n")
