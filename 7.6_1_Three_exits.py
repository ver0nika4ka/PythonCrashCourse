# Movie theater charges different ticket prices depending on a person’s age
print("Welcome to Aizu movie theater!")
age = input("\nPlease enter your age and I say how much ticket will cost for you: ")
age = int(age)
# Checking negative age
if age < 0:
    print("Sorry, I don't know this age!")
while age >= 0 :
    if age <= 3:
        print("\tTicket is free!")
    elif age > 3 and age <= 12:
        print("\tThe ticket is $10.")
    # Checking age >= 100
    elif age >= 100:
        print("You are lucky to live so long! \nYour ticket is free!") 
    else:
        print("\tThe ticket is $15.")
    # Program will ask to enter your age again and again
    # If you don't add 'input' here, program runs printing cost for entered age forever
    age = input("\nPlease enter your age and I say how much ticket will cost for you: ")
    age = int(age)
    # Checking negative age
    if age < 0:
        print("Sorry, I don't know this age!")

