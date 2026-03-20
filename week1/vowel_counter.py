# Ask the user for a word and convert it to lowercase
word = input("Enter a word: ").lower()

# Define vowels and initialize the counter
vowels = "aeiou"
count = 0

# Loop through each letter in the word and check if it is a vowel
for letter in word:
    if letter in vowels:              
        count += 1                # If the letter is a vowel, add +1 to the counter

# Display the total number of vowels
print(f"Number of vowels: {count}")
