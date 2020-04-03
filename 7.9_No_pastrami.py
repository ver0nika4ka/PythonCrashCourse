print("Sorry, the Deli restaurant has run out of 'pastrami'")
sandwich_orders = ['ham','cheese','salmon-avocado','peanut butter','pastrami']
finished_sandwiches = []
# Removing pastrami from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich...")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")