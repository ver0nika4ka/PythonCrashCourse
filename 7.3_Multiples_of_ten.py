# Ask user for a number, report whether the number is a multiple of 10 or not.
number = input("Please enter a number and I will tell you number is a multiple of 10 or not: ")
number = int(number)
remainder = number % 10
if remainder == 0:
    print(f"{number} is multiple of 10.")
else:
    print("Your number is NOT multiple of 10.")