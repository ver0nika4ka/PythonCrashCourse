# Program asks the user how many people are in their dinner group.
people = input("How many people in your dinner group?")
people = int(people)
if people > 8:
    print("\n You need to wait for a table.")
else:
    print("Your table is ready!")