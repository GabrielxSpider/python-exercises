# multiplication table
num = int(input("Please insert a number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# sum all numbers in a list
numbers = [50, 30, 10, 80]
total = 0
for number in numbers:
    total += number

print(total)

# finding the largest number
nums = [5, 8, 2, 10, 3]

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print(largest)

# reversing a string
word = input("Please type a word to be reversed: ")
reversed = ""

for letter in word:
    reversed = letter + reversed

print(reversed)