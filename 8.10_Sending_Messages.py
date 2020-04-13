def show_messages(messages):
    for message in messages:
        print(f"{message.title()}")

# Write a function, that prints each message and 
# Moves each message to a new list called sent_messages as it’s printed. 
def send_messages(messages, sent_messages):
    while messages:
        popped_message = messages.pop()
        print(f"Sending: {popped_message.title()}")
        sent_messages.append(popped_message)

# Make a list containing a series of short messages.
my_messages = ['hello', 'good morning','good evening','bye']
sent_messages = []

# Print message first
show_messages(my_messages)
# Sending messages to sent_messages
send_messages(my_messages, sent_messages)

# Print both lists to make sure the messages moved correctly.
print(f"Sent messages: {sent_messages}")
print(f"Initial messages: {my_messages}")