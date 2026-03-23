# count positive numbers
numbers = [-5, 10, 0, 8, -2, 3]

counter = 0

for positive in numbers:
    if positive >= 0:
        counter += 1
print(counter)

# count occurrences
nums = [1, 2, 2, 3, 4, 2, 5]
target = 2
count = 0

for num in nums:
    if target == num:
        count +=1
print(count)

# count each letter
word = input("Please input a word: ")
printed_letters = ""

for letter in word:
    if letter in printed_letters:
        continue

    count = 0

    for current_letter in word:
        if current_letter == letter:
            count += 1

    print(f"{letter}: {count}")
    printed_letters += letter
