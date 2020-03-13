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



