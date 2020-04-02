# Movie theater charges different ticket prices depending on a person’s age.
while True:
    age = input("\nPlease enter your age and I say how much ticket will cost for you: ")
    age = int(age)
    if age <= 3:
        print("Ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")
    exit_message = input("Do you want to exit? Enter 'yes'")
    if exit_message == 'yes' or exit_message == 'y' :
        break
