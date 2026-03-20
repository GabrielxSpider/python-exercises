# Define a list of numbers
numbers = [3, 7, 2, 9, 5]

# Get the first number using its index
largest = numbers[0]

# Loop through the list of numbers
for n in numbers:
    if n > largest:             # Check if the current number is greater than the current largest
        largest = n             # If it is, update the largest number

# Display the largest number found
print(largest)