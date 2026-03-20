# print numbers
to_ten = range(11)
print(list(to_ten))

# print numbers reversed
to_ten_reversed = range(10, 0, -1)
print(list(to_ten_reversed))

# print even numbers
to_ten_even = range(2, 21, 2)
print(list(to_ten_even))

# sum numbers from 1 to 100
to_hundred = list(range(0, 101))
total = 0
for number in to_hundred:
    total += number
print((total))

# count vowels in a string
intro = "Hello world!"
vowels = "aeiou"
counter = 0

for letter in intro:
    if letter in vowels:
        counter +=1
print(counter)

# print all letters of a string
word = input("Pleae digit a word: ")

for letter in word:
    print(letter)