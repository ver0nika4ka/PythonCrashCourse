# Guest list to invite for Birthday dinner

invited_guests = ['victor','gera','pyshkin','klyuev','vadim','liasan']
print(invited_guests)
message1 = 'Sorry to hear that you can not come '
print(f"{message1}, {invited_guests[-1].title()}!")
print(f"{message1}, {invited_guests[-2].title()}!")
invited_guests[4] = 'jeremy'
invited_guests[-1] = 'yu'
print(invited_guests)

message2 = 'Please come to my Birthday party'
print(f"{message2}, {invited_guests[0].title()}!")
print(f"{message2}, {invited_guests[1].title()}!")
print(f"{message2}, {invited_guests[2].title()}!")
print(f"{message2}, {invited_guests[3].title()}!")
print(f"{message2}, {invited_guests[4].title()}!")
print(f"{message2}, {invited_guests[-1].title()}!")

# add one guest to the end, next - to the beginning, and the last to the middle
invited_guests.append('jun')
invited_guests.insert(0,'naomi')
invited_guests.insert(4,'hamada')
print(invited_guests)
message3 = 'I found bigger place, so please come to my Birthday party'
print(f"{message3}, {invited_guests[0].title()}!")
print(f"{message3}, {invited_guests[1].title()}!")
print(f"{message3}, {invited_guests[2].title()}!")
print(f"{message3}, {invited_guests[3].title()}!")
print(f"{message3}, {invited_guests[4].title()}!")
#...
print(f"{message3}, {invited_guests[-1].title()}!")

message4 = 'Sorry, but I can invite only two people for a dinner :('
# in pop it is OK to leave brackets empty, no need to write invited_guests.pop(-1)
cannot_invite1 = invited_guests.pop()
cannot_invite2 = invited_guests.pop()
cannot_invite3 = invited_guests.pop()
cannot_invite4 = invited_guests.pop()
cannot_invite5 = invited_guests.pop()
cannot_invite6 = invited_guests.pop()
cannot_invite7 = invited_guests.pop()

print(f"{message4}, and you, {cannot_invite1.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite2.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite3.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite4.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite5.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite6.title()}, is not in that list!")
print(f"{message4}, and you, {cannot_invite7.title()}, is not in that list!")
#...
print(f"Dear {invited_guests[0].title()}, looking forward to meet you on today's Birthday dinner!")
print(f"Dear {invited_guests[1].title()}, looking forward to meet you on today's Birthday dinner!")

print(invited_guests)

del invited_guests[0]
del invited_guests[0]

print(invited_guests)







