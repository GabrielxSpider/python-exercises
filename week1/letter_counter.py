# Ask the user for a word
word = input("Enter a word: ")

# Remove spaces from the string
word_no_space = word.replace(" ", "")

# Display the number of letters
print("Number of letters:", len(word_no_space))