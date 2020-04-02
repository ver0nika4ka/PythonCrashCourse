# Movie theater charges different ticket prices depending on a person’s age
# Program runs forever and prints the price for added age.
print("Welcome to Aizu movie theater!")
age = input("\nPlease enter your age and I say how much ticket will cost for you: ")
age = int(age)
while age >= 0:
    if age <= 3:
        print("Ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")