# even or odd with try/except
try:
    num = int(input("Please input a integer number: "))

    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")    

except ValueError:
    print("That is not an integer.")

# hour adaptation challenger