"""Make a list or tuple containing a series of 10 numbers and five letters. 
Randomly select four numbers or letters from the list and print a message 
saying that any ticket with these four numbers or letters wins prize."""
from random import choice

num_letter = (3,8,'a',1,'z',7,5,'v',8,'x','q',0,9,2,4)

# Using list (shows e.g. ['v', 'a', 4, 'v'])
# ticket_num = []
# for i in range(4):
#     n = choice(num_letter)
#     ticket_num.append(n)

# Using strings (shows pretier e.g. 8x98 )
ticket_num = ''
for i in range(4):
    n = choice(num_letter)
    ticket_num += str(n)

print(f"Ticket matching this code wins a prize!"
    f"\nHere is a winning numbers and letters: {ticket_num}")
