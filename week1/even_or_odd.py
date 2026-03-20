# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number has a remainder when divided by 2
if number % 2 == 0:                  # If there is no remainder, it is even
    print("The number is even")
else:                                # If there is a remainder, it is odd
    print("The number is odd")