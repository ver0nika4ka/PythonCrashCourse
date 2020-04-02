# Movie theater charges different ticket prices depending on a person’s age
# Combined several tasks into one program
print("Welcome to Aizu movie theater!")
exit_message = 'no'
# Checking negative age
while exit_message != 'quit':
    age = input("\nPlease enter your age and I say how much ticket will cost for you: ")
    age = int(age)
    # Checking negative age
    if age < 0:
        print("Sorry, I don't know this age!")
    elif age <= 3:
        print("Ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket is $10.")
    # Checking age >= 100
    elif age >= 100:
        print("You are lucky to live so long! \nYour ticket is free!") 
    else:
        print("The ticket is $15.")
    exit_message = input("If you want to exit, enter 'quit': ")
    if exit_message == 'quit':
        break