print("Welcome to the Addition Program!")
print("Type 'quit' at any time to exit.\n")

while True:
    first = input("Enter the first number: ")
    if first.lower() == 'quit':
        print("Goodbye!")
        break

    second = input("Enter the second number: ")
    if second.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        num1 = int(first)
        num2 = int(second)
    except ValueError:
        print("Oops! You must enter numbers only. Please try again.\n")
    else:
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {total}.\n")