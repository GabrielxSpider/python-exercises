# simple menu
import randint
number = range(0,11)
while True: 
    print("1 - Say Hello!\n2 - Show random number\n3 - Leave")
    choice = int(input(""))
    if choice == 1:
        print("Hello!")
        continue
    elif choice == 2:
        print(randint(number))