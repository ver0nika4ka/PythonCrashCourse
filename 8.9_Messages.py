def show_messages(messages):
    for message in messages:
        print(f"{message.title()}")

# Make a list containing a series of short text messages.
my_messages = ['hello', 'good morning','good evening','bye']
# Pass the list to a function show_messages(), which prints each message.
show_messages(my_messages)