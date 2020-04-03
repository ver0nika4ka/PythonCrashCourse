sandwich_orders = ['ham','cheese','salmon-avocado','peanut butter']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich...")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")
