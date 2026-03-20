phrase = "Hello world, i am Python"

# Spliting the phrase into words
words = phrase.split()

counter = 0

# Goes through every word counting
for word in words:
    counter += 1   # Each word it counts adds +1 to counter
    
print(f"Your phrase has {counter} words.")