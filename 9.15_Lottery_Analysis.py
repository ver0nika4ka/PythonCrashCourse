"""Use a loop to see how hard it is to win the lottery you modeled. 
Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. 
Print a message how many times the loop run to give you a winning ticket."""

from random import choice

num_letter = (3,'c',8,'a',1,'z',7,5,'v',8,'x','p','o','q',0,'h','w',9,2,4,6,'k','f')
my_ticket = '8c1z'
count = 0

ticket_num = ''

while ticket_num != my_ticket:
    ticket_num = ''
    for i in range(4):
        n = choice(num_letter)
        ticket_num += str(n)
    count += 1

print(f"Your ticket won! Program run {count}")