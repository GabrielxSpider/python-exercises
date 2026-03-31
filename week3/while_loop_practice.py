# Password input

while True:
    password = input("Enter a password: ")
    if password == "python123":
        print("Correct password. Logging in...")
        break
    else:
        print("Incorrect password, try again.")

# Count until stop

while True:
    number = input("Enter a number (type 0 to exit): ")
    if number == "0":
        break

# Sum until exit

total = 0

while True:
    print("Type -1 to see the final sum")
    number = int(input("Enter a number to add: "))
    if number == -1:
        break
    total += number

print("Total sum:", total)
