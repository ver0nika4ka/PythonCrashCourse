favorite_numbers = {'alex': 10,
                    'david': 5,
                    'veronica': 7,
                    'victor': 3,
                    'alla': 3,
                    }
names = ['alex', 'david','veronica','victor','alla']
for name in names:
    print(f"{name.title()}'s favorite number: {favorite_numbers[name]}")