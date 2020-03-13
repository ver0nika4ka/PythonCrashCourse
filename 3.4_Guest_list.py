# Guest list to invite for Birthday dinner

invited_guests = ['victor','gera','pyshkin','klyuev','vadim','liasan']
print(invited_guests)
message = 'Please come to my Birthday party'
print(f"{message}, {invited_guests[0].title()}!")
print(f"{message}, {invited_guests[1].title()}!")

#1Using del
# del invited_guests[-1]
# del invited_guests[-1]

# print(invited_guests)

#2Using pop
# cannot_come1 = invited_guests.pop(-2)
# cannot_come2 = invited_guests.pop(-1)
# print(cannot_come1)
# print(cannot_come2)

#3Using remove to delete by value
# invited_guests.remove('vadim')
# invited_guests.remove('liasan')
# print(invited_guests)

#3.1Using remove, but first to add names who can not come to be able to print them after deleting
# cannot_come1 = 'vadim'
# cannot_come2 = 'liasan'
# invited_guests.remove(cannot_come1)
# invited_guests.remove(cannot_come2)
# print(cannot_come1)
# print(cannot_come2)
# print(invited_guests)