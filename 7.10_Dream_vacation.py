# Poll about dream vacation
responses = {}
# Set a flag to True
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    # Store the name and response in the dictionary.
    responses[name] = response
    repeat = input("Would you like to let another person to answer? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# Printing results of the poll.
print("--- Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")

