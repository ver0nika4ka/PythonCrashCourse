cities = {
    'tokyo': {
        'location':'japan',
        'population': '13 million',
        'fact': 'capital of Japan',
        },
    'minsk': {
        'location':'belarus',
        'population': '2 million',
        'fact': 'capital of Belarus',
        },
    'aizuwakamatsu': {
        'location':'japan',
        'population': '120 thousands',
        'fact': 'samurai city',
        },
    }
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value.title()}")

    # location = info['location']
    # population = info['population']
    # fact = info['fact']
    # print(f"\tLocation: {location.title()}")
    # print(f"\tPopulation: {population.title()}")
    # print(f"\tFact: {fact.title()}")
