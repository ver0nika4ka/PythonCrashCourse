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