# Ask the user for their full name
name = input("Enter your full name: ")

# Split the name and get only the first name
first_name = name.split()[0]

# Calculate the number of letters in the first name
length = len(first_name)

# Display the name in uppercase
print(name.upper())

# Display the name in lowercase
print(name.lower())

# Display the total number of letters (excluding spaces)
print(len(name.replace(" ", "")))

# Display the number of letters in the first name
print(length)