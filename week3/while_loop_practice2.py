# simple menu
total = 0

while True: 
    print("1 - Say Hello!\n2 - Add number to sum\n3 - Show total sum\n4 - Leave")
    choice = (input("-- Please insert a number: "))

    if choice == "1":
        print("Hello!\n")

    elif choice == "2":
        num = int(input("-- Input the number: ")) 
        total += num

    elif choice == "3":
        print(total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("-- Insert a valid number please. --")

# counter + sum

total = 0
quantity = 0

while True:
    digit = int(input("Please insert a number to sum, 0 to stop: "))

    if digit == 0:
        break

    total += digit
    quantity += 1

print(f"The sum is {total} of {quantity} numbers.")