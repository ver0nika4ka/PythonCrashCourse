rivers = {'nile': 'egypt',
        'amazon': 'brasil',
        'yangtze': 'china',
        'mekong': 'laos, cambodia, vietnam',
        'volga': 'russia',
        'ganges': 'india',
        'mississipi': 'united states',
        'danube': 'austria, hungary'
        }
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")