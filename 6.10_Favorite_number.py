favorite_numbers = {'alex': [10, 5],
                    'david': [2, 5],
                    'veronica': [3, 7],
                    'victor': [3, 33],
                    'alla': [8, 3],
                    }
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers: ")
    for numbers in numbers:
        print(f"{numbers}")