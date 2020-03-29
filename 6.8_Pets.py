dog = {'owner name': 'alex',
        'name': 'gosha',
        'breed': 'shiba inu',
        'color': 'white-brown',
        }
cat = {'owner name': 'nastya',
        'name': 'sema',
        'breed': 'bombay',
        'color': 'black',
        }
fish = {'owner name': 'sarah',
        'name': 'gilfoy',
        'breed': 'golden fish',
        'color': 'gold',
        }
pets =[dog, cat, fish]
for pet in pets:
    print("\nInfo about pet: ")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")